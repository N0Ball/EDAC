import json

from flask import Flask

from modules.edac.factory import EDACFactory
from modules.edac.schema import EDACType
from modules.noise.factory import NoiseFactory
from modules.noise.schema import NoiseType

app = Flask(__name__)

app.run()

@app.route("/")
def home():
    return "Hello, World"

@app.route("/parity/<message>")
def parity(message: str):

    try:
        message = message.encode('utf8')
        edac_system = EDACFactory(EDACType.PARITY)
        ENC_MSG = edac_system.encode(message)

        noise_system = NoiseFactory(NoiseType.BIT_FLIP)
        NOISE_MSG = noise_system.add_noise(ENC_MSG)

        pass_check, DEC_MSG, error_bits = edac_system.decode(NOISE_MSG)
    except Exception as e:
        return json.dumps({
            'error': e
        })

    return json.dumps({
        "encoded": str(ENC_MSG),
        "with_noise": str(NOISE_MSG),
        "decoded": [
            pass_check, str(DEC_MSG), error_bits
        ]
    })


@app.route("/parity/<message>/no_noise")
def parity_no_noise(message: str):

    try:
        message = message.encode('utf8')
        edac_system = EDACFactory(EDACType.PARITY)
        ENC_MSG = edac_system.encode(message)

        pass_check, DEC_MSG, error_bits = edac_system.decode(ENC_MSG)
    except Exception as e:
        return json.dumps({
            'error': e
        })

    return json.dumps({
        "encoded": str(ENC_MSG),
        "with_noise": str(ENC_MSG),
        "decoded": [
            pass_check, str(DEC_MSG), error_bits
        ]
    })