from modules import Debug
from .schema import NoiseMethod, NoiseType

class NoNoise(NoiseMethod):
    """A Noise system without any noise

    Args:
        debug (bool): the debug flag
    """

    def __init__(self, debug: Debug = Debug.DEPLOY) -> None:
        super().__init__(NoiseType.NO_NOISE, debug)

    def add_noise(self, data: int) -> int:
        """The Method of adding noise to the data

        Args:
            data (bytes): the data that is going to add noise on

        Returns:
            bytes: the data with noise
        """

        super().add_noise(data)

        if not self.DEBUG > Debug.DEBUG:
            print("LOG:\tusing <No Noise> for noise system")

        if not self.DEBUG > Debug.DEBUG:
            print(f"LOG:\tnoise system <No Noise> returned with {data}")

        return data