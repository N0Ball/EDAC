from Crypto.Util.number import bytes_to_long, long_to_bytes

from ..schema import EDACMethod, EDACType

class Parity(EDACMethod):
    """A [Parity](../../../../../tutorials/ErrorDetection/parity) 
    EDAC System to deal with data that needs parity code added

    Args:
        debug (bool, optional): Debug Level. Defaults to False.
    """

    def __init__(self, debug: bool= False) -> None:
        super().__init__(EDACType.PARITY, debug)
        self.DEFAULT_BLOCK = 8
        self.PARITY_SIZE = 1

    def encode(self, data: int) -> int:
        """encode the given integer (was bytes)

        Args:
            data (int): given integer

        Returns:
            int: integer that is encoded
        """

        # TODO add DEBUG message

        parity = 0
        while data > 0:
            parity ^= data&1
            data >>= 1

        return parity

    def decode(self, data: int, check: int) -> tuple:
        """Check the if the data is same as the given 
        parity code

        **See Also**

        - [EDACMethod](../../schema#decode)

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

        # TODO add debug message

        parity = 0
        tmp_data = data

        while tmp_data > 0:
            parity ^= tmp_data&1
            tmp_data >>= 1

        return (
            check == parity,
            0x0 if not check == parity else data,
            ["CI"] if not check == parity else [""]
        )