from abc import ABC, abstractmethod
from enum import Enum
import warnings

class EDACType(Enum):

    """Enumerate of the EDAC Type system
    """

    NO_EDAC = 'none'
    PARITY = 'parity'

class EDACMethod(ABC):

    """The Base class of the EDAC Method
    which means that all EDAC should contains all the methods
    it contains and will only be call the method it contains

    Args:
        TYPE ([EDACType](./#edactype)): The type of the EDAC system
        DEBUG (bool): Debug flag
    """

    def __init__(self, 
        edac_type: EDACType = EDACType.NO_EDAC, # Type of EDAC
        debug: bool=False # Debug Level
    ) -> None:

        self.TYPE: EDACType = edac_type
        self.DEBUG: bool = debug
        self.DEFAULT_BLOCK = None
        self.PARITY_SIZE = None

    def get_default_block(self) -> int:
        """Generate default block of the EDAC system

        Returns:
            int: default block of the EDAC system
        """

        if not self.DEFAULT_BLOCK:

            if self.DEBUG:
                warnings.warn("No Defualt block was given, using 8 bits")

            self.DEFAULT_BLOCk = 8


        return self.DEFAULT_BLOCK


    def get_parity_size(self) -> int:
        """Generate the parity size of the EDAC system

        Returns:
            int: parity size of the EDAC system
        """
        
        if not self.DEFAULT_BLOCK:

            if self.DEBUG:
                warnings.warn("No Defualt block was given, using 1 bit")

            self.PARITY_SIZE = 1

        return self.PARITY_SIZE

    @abstractmethod
    def encode(self, 
        data: int, # Data to be encode
    ) -> int:
        """The method that the EDAC system need to encode for futher
        EDAC usage

        Args:
            data (int): the data to be encoded

        Returns:
            int: the data encoded
        """
        pass

    @abstractmethod
    def decode(self,
        data: int, # Data to be decode
        check: int # Parity code
    ) -> tuple:
        """The method that the EDAC system need to decode for checking
        the correctness

        Args:
            data (int): The data to be checked
            check (int): Parity Code to check

        Returns:
            tuple: format should be `(error, data, error bits)`
            error (bool): Is the data corrupted
            data (bytes): The fixed data (return `0x00` if can't be fixed)
            error bits (list): The index of errorbits
        """
        pass