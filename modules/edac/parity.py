from modules import Debug
from .schema import EDACMethod, EDACType

class Parity(EDACMethod):
    """A [Parity](../../../../../tutorials/ErrorDetection/parity) 
    EDAC System to deal with data that needs parity code added

    Args:
        debug (bool, optional): Debug Level. Defaults to False.
    """

    def __init__(self, block_size: int = 8, debug: Debug = Debug.DEPLOY) -> None:
        super().__init__(EDACType.PARITY, debug)
        self.DEFAULT_BLOCK = block_size
        self.PARITY_SIZE = 1

    def _encode(self, data: int) -> int:
        """encode the given integer (was bytes)

        Args:
            data (int): given integer

        Returns:
            int: integer that is encoded
        """

        if not self.DEBUG > Debug.DEBUG:
            print(f"LOG:\tEncoding with EDAC Method: <Parity> with {bin(data)}")

        parity = 0
        while data > 0:
            parity ^= data&1
            data >>= 1

        if not self.DEBUG > Debug.DEBUG:
            print(f"LOG:\tResult of EDAC method: <Parity> is {parity}")

        return parity

    def _decode(self, 
        data: int, # Decode data
        check: int # Syndrome to be check
    ) -> tuple:
        """Check the if the data is same as the given 
        parity code

        Args:
            data (int): given data
            check (int): parity bit

        Returns:
            tuple: (**error**, **data**, **error bits**)
            error (bool): If any error happens in the data
            data (int): the corrected data (`0` for `CI`)
            error bits (list): the index of the error bits
            `CI` for `Cannot Identify`
        """

        if not self.DEBUG > Debug.DEBUG:
            print(f"LOG\tDecoding with EDAC Method: <Parity> with input {bin(data)}")

        parity = 0
        tmp_data = data

        while tmp_data > 0:
            parity ^= tmp_data&1
            tmp_data >>= 1

        if not self.DEBUG > Debug.DEBUG:
            print(f"LOG\tDecoded result for EDAC method <Parity> is {check == parity}")

        return (
            check == parity,
            None if not check == parity else data,
            ["CI"] if not check == parity else [""]
        )