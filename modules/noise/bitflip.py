import random

from modules import Debug
from .schema import NoiseType, NoiseMethod

class BitFlip(NoiseMethod):
    """Add the Bit Flip Noise System to the data

    Args:
        debug (Debug): the debug flag
        flip_list (list[int]): A list of integer index that defines the bit index\
            that should be flipped

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

    def __init__(self, flip_list: list = None, debug: Debug = Debug.DEPLOY) -> None:
        super().__init__(NoiseType.BIT_FLIP, debug)

        self.FLIP_LIST = flip_list

    def add_noise(self, data: int) -> int:
        """Validate the `flip_list` and add the noise to the data

        Args:
            data (int): The data to be noise added

        Raises:
            IndexError: the `flip_list` contains integers that exceeds the length of\
                the original data

        Returns:
            int: the data with the noise
        """

        super().add_noise(data)

        if not self.DEBUG > Debug.DEBUG:
            print("LOG:\tusing <Bit Flip> for noise system")

        # If the `flip_list` is empty, choose a random bit to flip
        if self.FLIP_LIST is None:
            
            if not self.DEBUG > Debug.WARNING:
                print("WARN:\tbit flip had not chosen a flip index, using random index!")
        
        # Checking if the index exceeds the maximum
        MAX = len(bin(data)[2:])
        if self.FLIP_LIST:
            # Check if any flip index is exceed the original data length
            for flip_index in self.FLIP_LIST:

                if flip_index >= MAX:
                    raise IndexError(f"Can't flip bit {flip_index} in {self.FLIP_LIST}: it's longer then the message")

        result = self.__add_noise(data)

        if not self.DEBUG > Debug.DEBUG:
            print(f"LOG:\tnoise system <Bit Flip> returned with {result}")

        return result

    def __add_noise(self, data: int) -> int:
        """The method to add noise

        Args:
            data (int): The data to add noise at

        Returns:
            int: the data with the noise

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

        data_len = len(bin(data)[2:])

        # Get a flip_list if flip_list is empty
        flip_list = self.FLIP_LIST if self.FLIP_LIST else [random.randint(0, data_len - 1)]

        # Debug messages to show the target flip index
        if not self.DEBUG > Debug.DEBUG:
            print(f"LOG:\tbit flip flipping index: {', '.join(map(str, flip_list))}")

        # Creates the mask to flip
        # remember, the $0^th$ data is actually the last data 
        # so `(data_len) - flip_index - 1` is use to inverse the index
        mask = 0
        for flip_index in flip_list:
            mask |= 1 << (data_len - flip_index - 1)

        # Flip the bits
        data ^= mask

        return data