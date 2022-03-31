from Crypto.Util.number import bytes_to_long, long_to_bytes

from ..schema import EDACMethod, EDACType

class Parity(EDACMethod):

    def __init__(self, debug: bool= False) -> None:
        super().__init__(EDACType.PARITY, debug)
        self.DEFAULT_BLOCK = 8
        self.PARITY_SIZE = 1

    def encode(self, data: int) -> int:

        parity = 0
        while data > 0:
            parity ^= data&1
            data >>= 1

        return parity

    def decode(self, data: int, check: int) -> tuple:

        parity = 0
        tmp_data = data

        while tmp_data > 0:
            parity ^= tmp_data&1
            tmp_data >>= 1

        return (
            check == parity,
            0xf if not check == parity else data,
            ["CI"] if not check == parity else [""]
        )