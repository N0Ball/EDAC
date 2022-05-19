from ..schema import EDACMethod, EDACType
from .crc_methods.schema import SCHEMA, GENERATOR

class CRC(EDACMethod):

    def __init__(self, debug: bool = False, *args, **kwargs) -> None:
        super().__init__(EDACType.CRC, debug)
        self.DEFAULT_BLOCK = 32
        self.PARITY_SIZE = None
        self.DEBUG = debug
        self.BIT = None
        self.GENERATOR = None

        try:
            self.__set_schema(kwargs['schema'])
        except KeyError:
            self.__set_schema(SCHEMA.CRC_8_ATM)
    
    def _generator_required(func):

        def wrapper(self, *args, **kwargs):

            if self.GENERATOR == None:

                self.GENERATOR = GENERATOR(SCHEMA.CRC_8_ATM)

                if self.DEBUG:
                    print(f"WARNING: No Generator had set, use default generator instead")

            return func(self, *args, **kwargs)

        return wrapper

    def __set_schema(self, schema: SCHEMA) -> None:
        
        self.GENERATOR = GENERATOR(schema)
        self.PARITY_SIZE = max(self.GENERATOR)

    def encode(self, data: int) -> int:
        
        data <<= max(self.GENERATOR)

        return self._devide(data)

    def decode(self, data: int, check: int) -> tuple:

        result = self._devide(data << max(self.GENERATOR)) == check

        return (
            result,
            data if result else 0x0,
            [""] if result else ["CI"]
        )

    @_generator_required
    def _devide(self, data: int) -> int:

        generator = sum(1 << e for e in self.GENERATOR)

        while not len(bin(data)) <= len(bin(generator)):
            generator <<= 1
        
        while not len(bin(data)) < max(self.GENERATOR):

            while not len(bin(data)) == len(bin(generator)):
                generator >>= 1

            data ^= generator

        return data ^ generator