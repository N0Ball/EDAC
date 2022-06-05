from .base import BaseView

from modules.edac import HammingCode as HC

class HammingCode(BaseView):

    def __init__(self):

        super().__init__('HammingCode', __name__)
        self.EDAC_METHOD = HC()