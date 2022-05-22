from .base import BaseView

from modules.edac.schema import EDACType

class Parity(BaseView):

    def __init__(self):
        super().__init__('parity', __name__)
        self.EDAC_TYPE = EDACType.PARITY