from modules.noise.schema import NoiseMethod

from modules.noise import NoNoise, BitFlip

class GenNoise:

    def __init__(self, method: NoiseMethod, args: dict) -> None:
        self.METHOD = method
        self.ARGS = args

    def _gen(self) -> NoiseMethod:
        pass

    def generate_noise(self) -> NoiseMethod:

        return self._gen()

class NoNoiseGenerator(GenNoise):

    def __init__(self, args: dict) -> None:
        super().__init__(NoNoise, args)

    def _gen(self) -> NoiseMethod:

        return self.METHOD()

class BitFlipGenerator(GenNoise):

    def __init__(self, args: dict) -> None:
        super().__init__(BitFlip, args)

    def _gen(self) -> NoiseMethod:

        self.flip_list = self.ARGS.get('flip_list', '').split(',')

        if not self.flip_list[0] == '':
            self.flip_list = list(map(int, self.flip_list))
        else:
            self.flip_list = []

        return self.METHOD(flip_list=self.flip_list)