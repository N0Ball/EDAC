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


        # Generate parity
        result_bytes = []
        for block in blocks:
            print(bin(self.EDAC_GEN.encode(block)))
            result_bytes.append((block<<self.PARITY_SIZE) + self.EDAC_GEN.encode(block))

        # Generate Result
        result = 0
        for result_byte in result_bytes:
            result += result_byte
            result <<= self.BLOCK_SIZE

        result >>= self.BLOCK_SIZE

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
        offset = len(bin(blocks[0])[2:])
        original_bytes = 0
        is_pass = True
        error_bits = []

        # Decode every blocks
        for block in blocks:

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

            # Generate the possible original bytes
            original_bytes <<= self.BLOCK_SIZE - self.PARITY_SIZE

        # Creates the bytes back
        while not len(bin(original_bytes)[2:])%self.BLOCK_SIZE == offset and not original_bytes == 0:
            original_bytes >>= 1

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

        # Change bytes to numerical
        from Crypto.Util.number import bytes_to_long
        _num_data = bytes_to_long(data)
        _blocks = []

        # Padding the bits
        _head_offset = 8 - len(bin(_num_data)[2:])%8
        while not (len(bin(_num_data)[2:]) + _head_offset) %n == 0:
            _num_data <<= 1

        # Making Blocks (inversed)
        while _num_data > 0:

            _blocks.append(_num_data & int('1'*n, 2))
            _num_data >>= n

        # Inverse back
        return _blocks[::-1]

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