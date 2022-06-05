from Crypto.Util.number import bytes_to_long, long_to_bytes

from modules.edac.schema import EDACMethod
from modules.noise.schema import NoiseMethod

class EDACTest:

    def __init__(self, msg: str, edac_method: EDACMethod, noise_method: NoiseMethod) -> None:
        self.MSG = bytes_to_long(msg.encode('utf8'))
        self.EDAC_METHOD = edac_method
        self.NOISE_METHOD = noise_method

    def run(self) -> dict:

        encode_msg = self._encode(self.MSG)

        noise_msg = self._add_noise(encode_msg)

        pass_check, decode_msg, error_bits = self._decode(noise_msg)
        decode_msg = long_to_bytes(decode_msg)

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


    def _encode(self, msg):

        encode_msg = self.EDAC_METHOD.encode(msg)

        return encode_msg

    def _add_noise(self, msg):

        noise_system = self.NOISE_METHOD
        noise_msg = noise_system.add_noise(msg)

        return noise_msg

    def _decode(self, msg):

        pass_check, decode_msg, error_bits = self.EDAC_METHOD.decode(msg)

        return (
            pass_check,
            decode_msg,
            error_bits
        )

