from .base import BaseView

from modules.edac import Parity as Pt

class Parity(BaseView):

    def __init__(self):
        super().__init__('parity', __name__)
        self.EDAC_METHOD = Pt()