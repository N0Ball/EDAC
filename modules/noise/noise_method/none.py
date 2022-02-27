from ..scheme import NoiseType, NoiseMethod

class NoNoise(NoiseMethod):
    """A Noise system without any noise

    Args:
        debug (bool): the debug flag
    """

    def __init__(self, debug: bool) -> None:
        super().__init__(NoiseType.NO_NOISE, debug)

    def add_noise(self, data: bytes) -> bytes:
        """The Method of adding noise to the data

        Args:
            data (bytes): the data that is going to add noise on

        Returns:
            bytes: the data with noise
        """
        return data