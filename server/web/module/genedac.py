from modules.edac.schema import EDACMethod

from modules.edac import HammingCode, Parity, CRC

class GenEDAC:

    def __init__(self, method: EDACMethod, args: dict) -> None:
        self.METHOD = method
        self.ARGS = args

    def _gen(self) -> EDACMethod:
        
        self.SIZE = self.ARGS.get('size', None)

        if self.SIZE is None:
            return self.METHOD()

        return self.METHOD(block_size=int(self.SIZE))

    def generate_edac(self) -> EDACMethod:

        return self._gen()

class ParityGenerator(GenEDAC):

    def __init__(self, args: dict) -> None:
        super().__init__(Parity, args)

class HammingCodeGenerator(GenEDAC):

    def __init__(self, args: dict) -> None:
        super().__init__(HammingCode, args)

class CRCGenerator(GenEDAC):

    def __init__(self, args: dict) -> None:
        super().__init__(CRC, args)
