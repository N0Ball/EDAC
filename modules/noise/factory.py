from .schema import NoiseType, NoiseMethod
from .methods.none import NoNoise
from .methods.bitflip import BitFlipNoise

class NoiseFactory:
    """Creates a noise system to add noise to.

    Args:
        noise_type ([NoiseType](../schema#NoiseType)): The noise type of the given type
        debug (bool, optional): The debug flag. Defaults to False.
        
    Example:
        >>> from lib.noise.schema import NoiseType
        >>> noise_system = NoiseFactory(NoiseType.NO_NOISE)
        >>> noise_system.add_noise(b"123")
        b'123'

    SeeAlso:
        [NoiseType](../schema#NoiseType)
    """

    def __init__(self, noise_type: NoiseType, debug: bool = False, **kwargs) -> None:
        self.TYPE: NoiseType = noise_type
        self.KWARGS: dict = kwargs
        self.DEBUG: bool = debug
        self.NOISE_GEN: NoiseMethod = self.__get_noise_generator(self.TYPE)

    def add_noise(self, data: bytes) -> bytes:
        """Add noise to the data

        Args:
            data (bytes): data to add noise on

        Raises:
            ValueError: data's type is not `bytes`

        Returns:
            bytes: the data with the noise
        """

        if not isinstance(data, bytes):
            raise ValueError(f'The input for a noise should be bytes')

        result = self.NOISE_GEN.add_noise(data)

        if self.DEBUG:
            print(f'ORIGINAL : {data}')
            print(f'WITHNOISE: {result}')

        return result

    def __get_noise_generator(self, noise_type: NoiseType) -> NoiseMethod:
        """Get the noise system of the given noise type

        Args:
            noise_type ([NoiseType](../schema#NoiseType)): the givin noise type seealso: noise.shceme.NoiseType

        Raises:
            ValueError: No noise type found

        Returns:
            NoiseMethod: the noise system
        """

        __noise_generator = {
            NoiseType.NO_NOISE: NoNoise(self.DEBUG),
            NoiseType.BIT_FLIP: BitFlipNoise(self.DEBUG, self.KWARGS)
        }.get(noise_type, None)

        if not __noise_generator:
            raise ValueError(f"No such Noise type: {noise_type}")

        return __noise_generator