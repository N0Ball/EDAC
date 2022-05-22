
from modules.edac.factory import EDACFactory
from modules.edac.schema import EDACType
from modules.noise.factory import NoiseFactory
from modules.noise.schema import NoiseType

class EDACTest:

    def __init__(self, msg: str, edac_type: EDACType, noise_type: NoiseType) -> None:
        self.MSG = msg.encode('utf8')
        self.EDAC_TYPE = edac_type
        self.NOSIE_TYPE = noise_type

    def run(self) -> dict:

        edac_system = EDACFactory(self.EDAC_TYPE)
        encode_msg = edac_system.encode(self.MSG)

        noise_system = NoiseFactory(self.NOSIE_TYPE)
        noise_msg = noise_system.add_noise(encode_msg)

        pass_check, decode_msg, error_bits = edac_system.decode(noise_msg)

        return {
            'original': str(self.MSG)[2:-1],
            'encode': str(encode_msg)[2:-1],
            'noise': str(noise_msg)[2:-1],
            'result': {
                'pass': pass_check,
                'decode': str(decode_msg)[2:-1],
                'errors': error_bits
            }
        }
            
