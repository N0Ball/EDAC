from .base import BaseView

from modules.edac.schema import EDACType

class HammingCode(BaseView):

    def __init__(self):

        super().__init__('HammingCode', __name__)
        self.EDAC_TYPE = EDACType.HAMMING_CODE