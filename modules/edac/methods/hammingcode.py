from Crypto.Util.number import bytes_to_long, long_to_bytes

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
        encoded_data = sum(map(lambda x: int(x[1]) << x[0], enumerate(bit_data)))
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

        for i in range(self.PARITY_SIZE - 1):
            
            if parity == 1 << i:
                parity = -1

        # Try to correct data (may be incorrect due to over two errors)
        if not parity == 0:
            bit_data[parity] ^= 1

        # Extract the parity bit
        parity_bit = bit_data.pop(0)

        # Recover decoded data
        data = sum(map(lambda x: int(x[1]) << x[0], enumerate(bit_data)))

        # TODO Fix this stupid thing
        # Since we have to transform back, so we have to add the parity bit back
        bit_data.insert(0, parity_bit)

        # Check parity bit
        check, data, status = self.PARITY_METHOD.decode(data, parity_bit)
        
        # Parity bit check fails
        if not check:
            return (
                False,
                0x0,
                ["CI"]
            )

        # Transform from hamming table to data
        for i in range(self.PARITY_SIZE - 2, -1, -1):
            bit_data.pop(1 << i)

            if parity > (1 << i):
                parity -= 1

        # Get rid of parity bit and the index offset cause by parity bit
        bit_data.pop(0)
        if not parity == 0:
            parity -= 1

        # Recover decoded data
        data = sum(map(lambda x: int(x[1]) << x[0], enumerate(bit_data[::-1])))

        # Return the hamming code result
        return (
            parity == 0,
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