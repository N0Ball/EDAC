from multiprocessing.sharedctypes import Value
from modules import Debug
from .schema import EDACMethod, EDACType
from .parity import Parity

class HammingCode(EDACMethod):
    """EDAC System to deal with data that needs hamming code 

    Args:
        debug (Debug, optional): Debug level. Defaults to False.
    """

    def __init__(self, block_size:int = 16, debug:Debug = Debug.DEPLOY) -> None:
        super().__init__(EDACType.HAMMING_CODE, debug)
        self.DEFAULT_BLOCK = block_size
        self.PARITY_METHOD = Parity(block_size, debug)

    def _encode(self, data: int) -> int:
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

        result = int(''.join(map(str, bit_data)), 2)
        parity = self.PARITY_METHOD.encode(result)&1

        result += parity << (self.DEFAULT_BLOCK - 1)

        # Return the result
        return result

    def _decode(self, data: int) -> tuple:
        """Decode the given data

        Args:
            data (int): the given data
            check (int): parity bytes

        Returns:
            tuple: the results of the decode [see more](../../schema#decode)
        """

        # Create hamming table
        bit_data = list(map(int, bin(data)[2:].rjust(self.BLOCK_SIZE, '0')))

        # Check parities and locate the incorrect bit
        parity = 0
        for i in range(self.BLOCK_SIZE):
            
            if bit_data[i]:
                parity ^= i

        # Try to correct data (may be incorrect while encounter over two errors)
        if not parity == 0:
            bit_data[parity] ^= 1

        # Recover decoded data
        data = int(''.join(map(str, bit_data)), 2)

        # Check parity bit
        is_pass, data, status = self.PARITY_METHOD.decode(data)

        # Parity check does not pass, recover the original incorrect data
        if not is_pass:
            bit_data[parity] ^= 1

        # Recover the original data
        # Get rid of parity bit
        for i in [1 << (self.PARITY_SIZE - 2 - e) for e in range(self.PARITY_SIZE - 1)]:

            bit_data.pop(i)

        bit_data.pop(0)
        data = int(''.join(map(str, bit_data)), 2)

        # Check Fails (Double Error Detected)
        if not is_pass and not parity == 0:

            return (
                False,
                data, 
                status
            )

        # Return the hamming code result
        return (
            True,
            data,
            [parity] if not parity == 0 else ([''] if is_pass else [0])
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

    def get_parity_size(self) -> int:

        if self.DEFAULT_BLOCK > 256:
            raise ValueError("ERROR: default block size is too large for hamming code")

        self.PARITY_SIZE = None

        for i in range(3, 9):

            if pow(2, i) == self.DEFAULT_BLOCK:
                self.PARITY_SIZE = i+1

        if self.PARITY_SIZE is None:
            raise ValueError("ERROR: block size must be a power of 2 (2^n), 8 >= n >= 3")

        return self.PARITY_SIZE