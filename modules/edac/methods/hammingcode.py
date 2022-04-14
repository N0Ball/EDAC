from Crypto.Util.number import bytes_to_long, long_to_bytes

from ..schema import EDACMethod, EDACType
from .parity import Parity

class HammingCode(EDACMethod):

    def __init__(self, debug: bool=False) -> None:
        super().__init__(EDACType.HAMMING_CODE, debug)
        self.DEFAULT_BLOCK = 16
        self.PARITY_SIZE = 5
        self.PARITY_METHOD = Parity(debug)

        assert pow(2, self.PARITY_SIZE - 1) == self.DEFAULT_BLOCK, "Wrong block or parity size"

    def encode(self, data: int) -> int:

        bit_data = self._create_table(data)

        for i, bit in enumerate(bit_data):

            for j in range(self.PARITY_SIZE - 1):

                if i >> j & 1:
                    bit_data[1 << j] ^= bit

        parity = 0
        for parity_bit in [bit_data[1 << i] for i in range(self.PARITY_SIZE - 1)]:
            parity += parity_bit
            parity <<= 1

        encoded_data = sum(map(lambda x: int(x[1]) << x[0], enumerate(bit_data)))
        parity += self.PARITY_METHOD.encode(encoded_data)

        return parity

    def decode(self, data: int, check: int) -> tuple:

        bit_data = self._create_table(data)
        
        bit_data[0] = check&1
        check >>= 1
        for i in range(self.PARITY_SIZE - 1):
            bit_data[1 << i] = check >> (self.PARITY_SIZE - i - 2) & 1

        parity = 0
        
        for i in range(self.DEFAULT_BLOCK):
            
            if bit_data[i]:
                parity ^= i

        if not parity == 0:
            bit_data[parity] ^= 1

        for i in range(self.PARITY_SIZE - 2, -1, -1):
            bit_data.pop(1 << i)

            if parity > (1 << i):
                parity -= 1

        bit_data.pop(0)
        if not parity == 0:
            parity -= 1

        print(parity)

        data = sum(map(lambda x: int(x[1]) << x[0], enumerate(bit_data)))

        check, data, status = self.PARITY_METHOD.decode(data, bit_data[0])
        
        if not check:
            return (
                False,
                0x0,
                ["CI"]
            )

        return (
            parity == 0,
            data,
            [parity] if not parity == 0 else [""]
        )

        
    def _create_table(self, data: int) -> list:

        table = [(data >> i)&1 for i in range(self.DEFAULT_BLOCK - self.PARITY_SIZE)]
        table = table[::-1]
        table.insert(0, 0)
        for i in range(self.PARITY_SIZE - 1):
            table.insert(1 << i, 0)
        
        return table