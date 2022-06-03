from modules import Debug
from Crypto.Util.number import long_to_bytes
from enum import Enum

class EDACType(Enum):

    """Enumerate of the EDAC Type system
    """

    NO_EDAC = 'none'
    PARITY = 'parity'
    HAMMING_CODE = 'hamming code'
    CRC = 'CRC'

class EDACMethod():

    """The Base class of the EDAC Method
    which means that all EDAC should contains all the methods
    it contains and will only be call the method it contains

    Args:
        TYPE ([EDACType](./#edactype)): The type of the EDAC system
        DEBUG (bool): Debug flag
    """

    def __init__(self, 
        edac_type: EDACType = EDACType.NO_EDAC, # Type of EDAC
        debug: Debug = Debug.DEPLOY # Debug Level
    ) -> None:

        self.TYPE: EDACType = edac_type
        self.DEBUG: Debug = debug
        self.DEFAULT_BLOCK = None
        self.PARITY_SIZE = None

    # Use field check to load the block size and parity size so that it can be modified after initalization
    def _field_check(func):

        def wrap(self, *args, **kwargs):

            self.BLOCK_SIZE = self.get_default_block()
            self.PARITY_SIZE = self.get_parity_size()

            return func(self, *args, **kwargs)

        return wrap

    def get_default_block(self) -> int:
        """Generate default block of the EDAC system

        Returns:
            int: default block of the EDAC system
        """

        if self.DEFAULT_BLOCK is None:
            
            print("ERROR: You are trying a method that doesn't have a default block. Every method needs a default block!")
            exit(1)

        return self.DEFAULT_BLOCK


    def get_parity_size(self) -> int:
        """Generate the parity size of the EDAC system

        Returns:
            int: parity size of the EDAC system
        """
        
        if self.PARITY_SIZE is None:
            
            print("ERROR: You are trying a method that doesn't have a parity size. Every method needs a parity size!")
            exit(1)

        return self.PARITY_SIZE

    @_field_check
    def encode(self, 
        data:int, # Data to be encode
        n: int=None # block size
    ) -> int:
        """The method that the EDAC system need to encode for futher
        EDAC usage

        Args:
            data (bytes): The data to be encoded
            n (int): The block size given (`None` as default)

        Returns:
            bytes: The data encoded
        """

        if not type(data) == int :
            raise ValueError("The input of the EDAC method of encoding should be <int>")

        if not self.DEBUG > Debug.DEBUG:
            print("LOG:\tTring to Encode")

        # Use the default block size of the edac method
        if n == None:
            n = self.BLOCK_SIZE

        # Creates block
        blocks = self._create_block(data, n - self.PARITY_SIZE)

        if not self.DEBUG > Debug.DEBUG:
            print(f"LOG:\tThe data had parsed to blocks: [{','.join(map(bin(blocks)))}]")

        # Generate result
        result = 0
        for block in blocks:
            
            result <<= n
            result += self._encode(block)

        # Return the result
        return result

    @_field_check
    def decode(self, data:int, n: int=None) -> tuple:
        """The method that the EDAC system need to decode for checking
        the correctness

        Args:
            data (bytes): The data to be decode

        Returns:
            tuple (bool, bytes, list): should be formated `(error, original data, error bits)`
        """

        if not self.DEBUG > Debug.DEBUG:
            print("LOG:\tTrying to Decode")

        # Use the default block size of the edac method
        if n == None:
            n = self.BLOCK_SIZE

        # Creates block
        blocks = self._create_block(data, n)
        decoded = 0
        is_pass = True
        error_bits = []

        # Decode every blocks
        for block in blocks:

            # Generate space for incomming bytes
            decoded <<= n - self.PARITY_SIZE

            # Decode the message
            error, fixed, error_list = self._decode(block)
            
            # store the results
            is_pass *= error
            error_bits += error_list

            # If can't fix, than return original data
            if not fixed is None:
                decoded += fixed
            else:
                decoded += block

        return (is_pass, decoded, error_bits)

    def _create_block(self,
        data: int,
        n: int
    ) -> list:

        """Parse data into blocks so that
        every block have n bits of data

        Raises:
            ValueError: If the data's type isn't `bytes`

        Returns:
            list: the list of blocks needed
        """

        if not isinstance(data, int):
            raise ValueError("The type of data should be type <int>")

        bin_string = bin(data)[2:]
        LEN = len(bin_string)

        if not LEN%n == 0:
            bin_string = '0'*(n - LEN%n) + bin_string

        # Create blocks
        blocks = []

        while len(bin_string) > 0:

            element = int(bin_string[:n], 2)
            bin_string = bin_string[n:]

            blocks.append(element)

        return blocks

    def _parse_parity(
        self, 
        data:int
    ) -> tuple:

        parity = data&int('1'*self.PARITY_SIZE)
        data >>= self.PARITY_SIZE

        return (data, parity)