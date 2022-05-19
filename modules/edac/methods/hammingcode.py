from ..schema import EDACMethod, EDACType
from .parity import Parity

class HammingCode(EDACMethod):
    """EDAC System to deal with data that needs hamming code 

    Args:
        debug (bool, optional): Debug level. Defaults to False.
    """

    def __init__(self, debug: bool=False) -> None:
        super().__init__(EDACType.HAMMING_CODE, debug)
        self.DEFAULT_BLOCK = 16
        self.PARITY_SIZE = 5
        self.PARITY_METHOD = Parity(debug)

        assert pow(2, self.PARITY_SIZE - 1) == self.DEFAULT_BLOCK, "Wrong block or parity size"

    def encode(self, data: int) -> int:
        """Encode the given data

        Args:
            data (int): the data in integer

        Returns:
            int: the encoded data in integer
        """

        # Create hamming code table
        bit_data = self._create_table(data)

        # Create parity bytes
        for i, bit in enumerate(bit_data):

            for j in range(self.PARITY_SIZE - 1):

                if i >> j & 1:
                    bit_data[1 << j] ^= bit

        # Encode parity bytes
        parity = 0
        for parity_bit in [bit_data[1 << i] for i in range(self.PARITY_SIZE - 1)]:
            parity += parity_bit
            parity <<= 1

        # Add parity bit
        encoded_data = int(''.join(map(str, bit_data)), 2)
        parity += self.PARITY_METHOD.encode(encoded_data)

        # Return the result
        return parity

    def decode(self, data: int, check: int) -> tuple:
        """Decode the given data

        Args:
            data (int): the given data
            check (int): parity bytes

        Returns:
            tuple: the results of the decode [see more](../../schema#decode)
        """

        # Create hamming table
        bit_data = self._create_table(data)
        
        # Get parity bit
        bit_data[0] = check&1
        check >>= 1

        # Put hammingcode's parity byte to the hamming table
        for i in range(self.PARITY_SIZE - 1):
            bit_data[1 << i] = check >> (self.PARITY_SIZE - i - 2) & 1

        parity = 0
        
        # Check parities and locate the incorrect bit
        for i in range(self.DEFAULT_BLOCK):
            
            if bit_data[i]:
                parity ^= i

        # Check if the error belongs to parity bit
        if parity in [(1 << e) for e in range(self.PARITY_SIZE)]:
            bit_data[0] ^= 1
            parity = -1

        # Try to correct data (may be incorrect due to over two errors)
        if not (parity == 0 or parity == -1):
            bit_data[parity] ^= 1

        # Recover decoded data
        data = int(''.join(map(str, bit_data[1:])), 2)

        # Check parity bit
        check, data, status = self.PARITY_METHOD.decode(data, bit_data[0])
        
        # Parity bit check fails
        if not check:
            return (
                False,
                None,
                status
            )

        # Get rid of parity bit and the index offset cause by parity bit
        for i in [1 << (self.PARITY_SIZE - 2 - e) for e in range(self.PARITY_SIZE - 1)]:

            bit_data.pop(i)

            if parity > i:
                parity -= 1

        bit_data.pop(0)
        if parity > 0:
            parity -= 1

        # Recover decoded data
        data = int(''.join(map(str, bit_data)), 2)

        # Return the hamming code result
        return (
            True,
            data,
            [parity] if not parity == 0 else [""]
        )

        
    def _create_table(self, data: int) -> list:
        """Create the hamming table according to the given block size

        Args:
            data (int): data

        Returns:
            list: hamming table
        """         
        
        # Create a inverse table
        table = [(data >> i)&1 for i in range(self.DEFAULT_BLOCK - self.PARITY_SIZE)]
        
        # Inverse back
        table = table[::-1]

        # Create parity bit storage
        table.insert(0, 0)

        # Create hamming code parity byte storage
        for i in range(self.PARITY_SIZE - 1):
            table.insert(1 << i, 0)
        
        # Finish creating table
        return table