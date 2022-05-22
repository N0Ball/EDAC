from flask import Blueprint

from ..module.edactest import EDACTest

from modules.noise.schema import NoiseType

class BaseView:

    def __init__(self, route_name:str, name) -> None:
        self.ROUTE = Blueprint(route_name, name)
        self.EDAC_TYPE = None

    def get_route(self):

        @self.ROUTE.route("/<message>")
        def default(message: str):

            return self._run_test(message, NoiseType.BIT_FLIP)

        @self.ROUTE.route("/<message>/no_noise")
        def no_noise(message: str):

            return self._run_test(message, NoiseType.NO_NOISE)

        return self.ROUTE

    def _run_test(self, message: str, noise_type: NoiseType):

        try:

            test = EDACTest(message, self.EDAC_TYPE, noise_type)
            return test.run()

        except Exception as e:
            return {
                'error': e
            }