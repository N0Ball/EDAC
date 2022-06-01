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
        data:bytes, # Data to be encode
        n: int=None # block size
    ) -> bytes:
        """The method that the EDAC system need to encode for futher
        EDAC usage

        Args:
            data (bytes): The data to be encoded
            n (int): The block size given (`None` as default)

        Returns:
            bytes: The data encoded
        """

        if not type(data) == bytes :
            raise ValueError("The input of the EDAC method of encoding should be <bytes>")

        if not self.DEBUG > Debug.DEBUG:
            print("LOG:\tTring to Encode")

        # Use the default block size of the edac method
        if n == None:
            n = self.BLOCK_SIZE

        # Creates block
        blocks = self._create_block(data, n - self.PARITY_SIZE)

        # Generate result
        result = 0
        for block in blocks:
            
            result <<= self.BLOCK_SIZE
            result += (block<<self.PARITY_SIZE) + self._encode(block)

        # Return the result
        return long_to_bytes(result)

    @_field_check
    def decode(self, data:bytes, n: int=None) -> tuple:
        """The method that the EDAC system need to decode for checking
        the correctness

        Args:
            data (bytes): The data to be decode

        Returns:
            tuple (bool, bytes, list): should be formated `(error, original data, error bits)`
        """

        # Use the default block size of the edac method
        if n == None:
            n = self.BLOCK_SIZE

        # Creates block
        blocks = self._create_block(data, self.BLOCK_SIZE)
        original_bytes = 0
        is_pass = True
        error_bits = []

        # Decode every blocks
        for block in blocks:

            # Generate space for incomming bytes
            original_bytes <<= self.BLOCK_SIZE - self.PARITY_SIZE

            # Get the parity bit out
            original_data = block >> self.PARITY_SIZE
            parity = block & int('1' * self.PARITY_SIZE, 2)

            # Decode the message
            error, fixed, error_list = self._decode(original_data, parity)
            
            # store the results
            is_pass *= error
            error_bits += error_list

            # If can't fix, than return original data
            if not fixed is None:
                original_bytes += fixed
            else:
                original_bytes += original_data

        # Get rid of the paddings
        decode_size = len(long_to_bytes(original_bytes))
        data_size = self.BLOCK_SIZE - self.PARITY_SIZE

        if decode_size > 1 and not (decode_size*8) % data_size == 0:
            original_bytes >>= data_size - ((decode_size - 1)*8)%data_size

        return (is_pass, long_to_bytes(original_bytes), error_bits)
    # def encode(self, 
    #     data: int, # Data to be encode
    # ) -> int:
    #     """The method that the EDAC system need to encode for futher
    #     EDAC usage

    #     Args:
    #         data (int): the data to be encoded

    #     Returns:
    #         int: the data encoded
    #     """
    #     pass

    # def decode(self,
    #     data: int, # Data to be decode
    #     check: int # Parity code
    # ) -> tuple:
    #     """The method that the EDAC system need to decode for checking
    #     the correctness

    #     Args:
    #         data (int): The data to be checked
    #         check (int): Parity Code to check

    #     Returns:
    #         tuple: format should be `(error, data, error bits)`
    #         error (bool): Is the data corrupted
    #         data (bytes): The fixed data (return `0x00` if can't be fixed)
    #         error bits (list): The index of errorbits
    #     """
    #     pass

        
    def _create_block(self,
        data: bytes,
        n: int
    ) -> list:

        """Parse data into blocks so that
        every block have n bits of data

        Raises:
            ValueError: If the data's type isn't `bytes`

        Returns:
            list: the list of blocks needed
        """

        if not isinstance(data, bytes):
            raise ValueError("The type of data should be bytes")

        # Byte to binary string
        bin_string = ''.join(map(lambda x: bin(x)[2:].rjust(8, '0'), data))

        # Create blocks
        blocks = []

        while not bin_string == '0'*n:

            element = int(bin_string[:n], 2)
            bin_string = bin_string[n:].ljust(n, '0') # Append 0 if needed

            blocks.append(element)

        return blocks