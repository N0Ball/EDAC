import random
import warnings
from Crypto.Util.number import long_to_bytes, bytes_to_long

from ..schema import NoiseType, NoiseMethod

class BitFlipNoise(NoiseMethod):
    """Add the Bit Flip Noise System to the data

    Args:
        debug (bool): the debug flag
        kwargs (optional): The key word argument passed from \
            [Noise Factory](../../noise/). Defaults to None.\
            should contain key `flip_list`
        flip_list (list[int]): A list of integer index that defines the bit index\
            that should be flipped

    Note:
        the `**kwargs` should be `flip_list (list[int])`, if no such key in\
            `**kwargs` it will auto flips a random bit

    Example:

        >>> from lib.noise.noise import NoiseFactory
        >>> from lib.noise.schema import NoiseType
        >>> noise_system = NoiseFactory(NoiseType.BIT_FLIP, flip_list=[6])
        >>> noise_system.add_noise(b'OUO')
        b'MUO'
        >>> noise_system.add_noise(b'OUO')
        b'MUO'
        >>> noise_system = NoiseFactory(NoiseType.BIT_FLIP)
        >>> noise_system.add_noise(b'OUO')
        b'OuO'
        >>> noise_system.add_noise(b'OUO')
        b'O\xd5O'
    """

    def __init__(self, debug: bool, kwargs: dict = None) -> None:
        super().__init__(NoiseType.BIT_FLIP, debug)

        # Set the bits to flip (by index)
        try:
            self.FLIP_LIST = kwargs['flip_list']
        except KeyError:
            self.FLIP_LIST = None

    def add_noise(self, data: bytes) -> bytes:
        """Validate the `flip_list` and add the noise to the data

        Args:
            data (bytes): The data to be noise added

        Raises:
            IndexError: the `flip_list` contains integers that exceeds the length of\
                the original data

        Returns:
            bytes: the data with the noise
        """

        MAX = len(data)*8

        # If the `flip_list` is empty, choose a random bit to flip
        if not self.FLIP_LIST and self.DEBUG:
            warnings.warn(f'No flip_list found, use random')
        
        if self.FLIP_LIST:
            # Check if any flip index is exceed the original data length
            for flip_index in self.FLIP_LIST:

                if flip_index >= MAX:
                    raise IndexError(f"Can't flip bit {flip_index} in {self.FLIP_LIST}: it's longer then the message")

        return self.__add_noise(data)

    def __add_noise(self, data: bytes) -> bytes:
        """The method to add noise

        Args:
            data (bytes): The data to add noise at

        Returns:
            bytes: the data with the noise

        Note:
            The algorithm of this method is using a xor mask to flip the data\
               , since `x ^ 0 = x, x ^ 1 = !x`
            Given an example

            ```
            | 0 | 1 | 2 | 3 | 4 |

            | 1 | 0 | 1 | 1 | 0 |
            --------------------- XOR
            | 0 | 0 | 1 | 0 | 1 |
            --------------------- Results
            | 1 | 0 |*0*| 1 |*1*|
            ```

            You can see that except the \(2^{nd}\) and the \(4^{th}\) data, the data remains\
                the same.

        """

        data_len = len(data) * 8

        # Convert the data to integer
        int_data = bytes_to_long(data)

        # Get a flip_list if flip_list is empty
        flip_list = self.FLIP_LIST if self.FLIP_LIST else [random.randint(0, data_len - 1)]

        # Debug messages to show the target flip index
        if self.DEBUG:
            print(f"FLIPING-INDEX: {', '.join(map(str, flip_list))}")

        # Creates the mask to flip
        # remember, the $0^th$ data is actually the last data 
        # so `(data_len) - flip_index - 1` is use to inverse the index
        mask = 0
        for flip_index in flip_list:
            mask |= 1 << (data_len - flip_index - 1)

        # Flip the bits
        int_data ^= mask

        # Convert the integer back to the data
        data = long_to_bytes(int_data)

        return data