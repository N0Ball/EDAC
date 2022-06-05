from flask import Blueprint

from ..module.edactest import EDACTest

from modules.noise import NoNoise, BitFlip
from modules.noise.schema import NoiseMethod

class BaseView:

    def __init__(self) -> None:
        self.ROUTE = Blueprint('noise', __name__)
        self.EDAC_METHOD = None

    def get_route(self):

        @self.ROUTE.route("/<message>")
        def default(message: str):

            return self._run_test(message, BitFlip())

        @self.ROUTE.route("/<message>/no_noise")
        def no_noise(message: str):

            return self._run_test(message, NoNoise())

        @self.ROUTE.route("<message>/bit_flip/<flip_list>")
        def bit_flip(message: str, flip_list: str):

            import json

            try:
                flip_list = json.loads(flip_list)
                return self._run_test(message, BitFlip(flip_list=flip_list))
            except Exception as e:
                return {
                    'error': str(e)
                }

        return self.ROUTE

    def _run_test(self, message: str, noise_type: NoiseMethod):

        try:

            test = EDACTest(message, self.EDAC_METHOD, noise_type)
            return test.run()

        except Exception as e:
            return {
                'error': str(e)
            }