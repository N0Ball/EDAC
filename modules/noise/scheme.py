from abc import ABC, abstractmethod

class NoiseType:

    """The Noise type Enumerate of the Noise system
    
    Attributes:
        NO_NOISE (A system with no Noise): see also [NO_NOISE](../systems/NO_NOISE/)
        BIT_FLIP (A system that flip bits): see also [BIT_FLIP](../systems/BIT_FLIP/)
    """

    NO_NOISE = 0
    BIT_FLIP = 1

class NoiseMethod(ABC):

    """The Base class fo the Noise Method

    Args:
        TYPE (NoiseType): The type of noise system
        DEBUG (bool): Debug Flag

    Note:
        This is the abstract base class, `add_noise` method should **never be called**
    """

    def __init__(self, noise_type: NoiseType = NoiseType.NO_NOISE, debug: bool = False) -> None:
        self.TYPE = noise_type
        self.DEBUG = debug

    @abstractmethod
    def add_noise(self, data: bytes) -> bytes:
        """Add the noise to the data from the noise system

        Args:
            data (bytes): the data that the noise is going to add on

        Returns:
            bytes: the data with the noise
        """
        pass