from flask import Flask

from .routes.parity import Parity
from .routes.hammingcode import HammingCode

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World"

from flask import request, abort

from .module.edactest import EDACTest
from .module.gennoise import BitFlipGenerator, NoNoiseGenerator
from .module.genedac  import HammingCodeGenerator, ParityGenerator, CRCGenerator

from modules.noise.schema import NoiseMethod
from modules.edac.schema import EDACMethod

@app.route("/test")
def default():

    data = request.args['data']
    noise_type = request.args['noise']
    edac_type = request.args['edac']

    NOISE_METHOD = _get_noise(noise_type, request.args)
    EDAC_METHOD = _get_edac(edac_type, request.args)

    return _run_test(NOISE_METHOD, EDAC_METHOD, data)


def _get_noise(noise_type: str, args: dict) -> NoiseMethod:

    result = {
        'no_noise': NoNoiseGenerator(args),
        'bit_flip': BitFlipGenerator(args)
    }.get(noise_type, None)

    if result is None:
        abort(400, 'bad noise type')

    return result.generate_noise()

def _get_edac(edac_type: str, args: dict) -> EDACMethod:

    result = {
        'hamming_code': HammingCodeGenerator(args),
        'crc': CRCGenerator(args),
        'parity': ParityGenerator(args)
    }.get(edac_type, None)

    if result is None:
        abort(400, 'bad edac type')

    return result.generate_edac()

def _run_test(noise_method, edac_method, message: str):

    try:

        test = EDACTest(message, edac_method, noise_method)
        return test.run()

    except Exception as e:
        return {
            'error': str(e)
        }

app.register_blueprint(Parity().get_route(), url_prefix='/parity')
app.register_blueprint(HammingCode().get_route(), url_prefix='/hammingCode')

if __name__ == '__main__':
    app.run()