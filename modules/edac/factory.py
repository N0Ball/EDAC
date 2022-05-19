from Crypto.Util.number import long_to_bytes, bytes_to_long

from .schema import EDACType, EDACMethod

from .methods import *

class EDACFactory:
    """Creates the EDAC System specify by given [EDAC Type](../schema/#edactype)

    Args:
        edac_type ([EDACType](../schema/#edactype)): The EDAC type needed
        debug (bool): Debug Level
    """

    def __init__(self,
        edac_type: EDACType,
        debug: bool = False,
        **kwargs
    ) -> None:

        self.TYPE: EDACType = edac_type
        self.DEBUG: bool = debug
        self.KWARGS: dict = kwargs
        self.EDAC_GEN: EDACMethod = self.__get_edac_generator(self.TYPE)

    # Use field check to load the block size and parity size so that it can be modified after initalization
    def _field_check(func):

        def wrap(self, *args, **kwargs):

            self.BLOCK_SIZE = self.EDAC_GEN.get_default_block()
            self.PARITY_SIZE = self.EDAC_GEN.get_parity_size()

            return func(self, *args, **kwargs)

        return wrap

    @_field_check
    def encode(self, data:bytes, n: int=None) -> bytes:
        """Encodes the data with edac system

        Args:
            data (bytes): The data to be encoded
            n (int): The block size given (`None` as default)

        Returns:
            bytes: The data encoded
        """

        # Use the default block size of the edac method
        if n == None:
            n = self.BLOCK_SIZE

        # Creates block
        blocks = self._create_block(data, self.BLOCK_SIZE - self.PARITY_SIZE)

        # Generate result
        result = 0
        for block in blocks:
            
            result <<= self.BLOCK_SIZE
            result += (block<<self.PARITY_SIZE) + self.EDAC_GEN.encode(block)

        return long_to_bytes(result)

    @_field_check
    def decode(self, data:bytes, n: int=None) -> tuple:
        """Decodes the data to verify the integrity

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
            error, fixed, error_list = self.EDAC_GEN.decode(original_data, parity)
            
            # store the results
            is_pass *= error
            error_bits += error_list

            # TODO This is not used anymore
            if not fixed == None:
                original_bytes += fixed
            else:
                original_bytes += original_data

        # Get rid of the paddings
        decode_size = len(long_to_bytes(original_bytes))
        data_size = self.BLOCK_SIZE - self.PARITY_SIZE

        if decode_size > 1 and not (decode_size*8) % data_size == 0:
            original_bytes >>= data_size - ((decode_size - 1)*8)%data_size

        return (is_pass, long_to_bytes(original_bytes), error_bits)

    
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


    def __get_edac_generator(self,
        edac_type: EDACType # Type of EDAC system
    ) -> EDACMethod:

        """Get the edac system specified by [EDACType](../schema/#edactype)

        Raises:
            ValueError: If no EDAC Type was found

        Returns:
            [EDACMethod](../schema/#edacmethod): EDAC system 
        """

        __edac_generator = {
            EDACType.PARITY: parity.Parity(self.DEBUG),
            EDACType.HAMMING_CODE: hammingcode.HammingCode(self.DEBUG),
            EDACType.CRC: crc.CRC(self.DEBUG, self.KWARGS)
        }.get(edac_type, None)

        if not __edac_generator:
            raise ValueError(f"No such EDAC type: {edac_type}")

        return __edac_generator