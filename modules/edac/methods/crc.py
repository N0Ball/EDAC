from ..schema import EDACMethod, EDACType
from .crc_methods.schema import SCHEMA, GENERATOR

class CRC(EDACMethod):
    """EDAC System to deal with data that needs CRC

    Args:
        debug (bool, optional): Debug level. Defualts to False.
        kwargs (optional): The keyword argument passed from \
            [EDAC Factory](../../factory#EDACFactory). Defualts to None.\
            **should contian key `schema`**
        schema ([SCHEMA](../crc_methods/schema#SCHEMA)): The schema of\
            CRC you chose to use, defaults to `CRC_8_ATM`

    """

    def __init__(self, debug: bool = False, *args, **kwargs) -> None:
        super().__init__(EDACType.CRC, debug)
        self.DEFAULT_BLOCK = 32
        self.PARITY_SIZE = None
        self.DEBUG = debug
        self.BIT = None
        self.GENERATOR = None

        # Get the Schema of CRC Type, default sets to CRC 8 ATM
        try:
            self.__set_schema(kwargs['schema'])
        except KeyError:
            self.__set_schema(SCHEMA.CRC_8_ATM)
    
    # Check if generator had already exist
    def _generator_required(func):

        def wrapper(self, *args, **kwargs):

            if self.GENERATOR == None:

                self.GENERATOR = GENERATOR(SCHEMA.CRC_8_ATM)

                if self.DEBUG:
                    print(f"WARNING: No Generator had set, use default generator instead")

            return func(self, *args, **kwargs)

        return wrapper

    # Set the schema
    def __set_schema(self, schema: SCHEMA) -> None:
        
        self.GENERATOR = GENERATOR(schema)
        self.PARITY_SIZE = max(self.GENERATOR)

    def encode(self, data: int) -> int:
        """Encode the given data

        Args:
            data (int): the data in integer

        Returns:
            int: the syndrome in interger
        """
        
        # Append for the parity size
        data <<= self.PARITY_SIZE

        # Return the result
        return self._devide(data)

    def decode(self, data: int, check: int) -> tuple:
        """Decode the given data

        Args:
            data (int): the target data to decode
            check (int): syndrome

        Returns:
            tuple: the results of the decode [see more](../../schema#decode)

        """

        # Simply checks if the result is 0 
        result = self._devide(data << self.PARITY_SIZE + check)

        return (
            result,
            data if result else None,
            [""] if result else ["CI"]
        )

    @_generator_required
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
        
        while not len(bin(data)) < max(self.GENERATOR):

            while not len(bin(data)) == len(bin(generator)):
                generator >>= 1

            data ^= generator

        return data ^ generator