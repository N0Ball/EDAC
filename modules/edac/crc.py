from modules import Debug

from .schema import EDACMethod, EDACType
from .methodschema.crc import SCHEMA, GENERATOR

class CRC(EDACMethod):
    """EDAC System to deal with data that needs CRC

    Args:
        debug (Debug, optional): Debug level. Defualts to Deploy.
        kwargs (optional): The keyword argument passed from \
            [EDAC Factory](../../factory#EDACFactory). Defualts to None.\
            **should contian key `schema`**
        schema ([SCHEMA](../crc_methods/schema#SCHEMA)): The schema of\
            CRC you chose to use, defaults to `CRC_8_ATM`

    """

    def __init__(self, block_size: int = 40,  type: SCHEMA = None, debug: Debug = Debug.DEPLOY) -> None:
        super().__init__(EDACType.CRC, debug)
        self.DEFAULT_BLOCK = block_size
        self.SCHEMA = type
        self.DEBUG = debug
        self.BIT = None
        self.GENERATOR = None
    
    # Check if generator had already exist
    def _generator_required(func):

        def wrapper(self, *args, **kwargs):

            if self.SCHEMA is None:

                self.SCHEMA = SCHEMA.CRC_8_ATM
                self.GENERATOR = GENERATOR(SCHEMA.CRC_8_ATM)

                if not self.DEBUG > Debug.WARNING:
                    print(f"WARNING: No Generator had set, use default generator instead")

            else:

                self.GENERATOR = GENERATOR(self.SCHEMA)

                if not self.DEBUG > Debug.DEBUG:
                    print(f"LOG\tCRC schema set to <{self.SCHEMA}>")


            return func(self, *args, **kwargs)

        return wrapper

    def get_parity_size(self) -> int:

        self.__set_schema()

        return super().get_parity_size()

    @_generator_required
    # Set the schema
    def __set_schema(self) -> None:
        
        self.PARITY_SIZE = max(self.GENERATOR)

    def _encode(self, data: int) -> int:
        """Encode the given data

        Args:
            data (int): the data in integer

        Returns:
            int: the syndrome in interger
        """
        
        # Append for the parity size
        data <<= self.PARITY_SIZE
        # Get the parity
        parity = self._devide(data)

        # Return the result
        return data + parity

    def _decode(self, data: int) -> tuple:
        """Decode the given data

        Args:
            data (int): the target data to decode

        Returns:
            tuple: the results of the decode [see more](../../schema#decode)

        """

        # Simply checks if the result is 0 
        result = self._devide(data)

        return (
            result == 0,
            data >> self.PARITY_SIZE,
            [""] if result == 0 else ["CI"]
        )

    def _devide(self, data: int) -> int:
        """Devide in GF(\(2^n\)) of given generator

        Args:
            data (int): the given data

        Returns:
            int: the result
        """

        generator = sum(1 << e for e in self.GENERATOR)

        while not len(bin(data)) <= len(bin(generator)):
            generator <<= 1
        
        while not len(bin(data)[2:]) <= max(self.GENERATOR):

            while not len(bin(data)) == len(bin(generator)) and len(bin(generator)[2:]) > max(self.GENERATOR):
                generator >>= 1

            data ^= generator

        return data