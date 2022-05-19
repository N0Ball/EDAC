import unittest
import yaml

def get_test_data(name):

    with open(f'./tests/data/{name}.yml') as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        testfuncs = dat['tests']

        parameters = {}

        for tests in testfuncs:

            case = []
            data = []
            expected = []

            for td in testfuncs[tests]:
                case.append(td.get('case', ''))
                data.append(td.get('data', {}))
                expected.append(td.get('expected', {}))

            parameters[tests] = zip(case, data, expected)

    return parameters

class TestBase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        test_name = self.__module__.split('.')[-1][5:]
        self.TEST_DATA = get_test_data(test_name)

    def parameterized(func):

        def wrapper(self):

            test_type = self._testMethodName[5:]

            for case in self.TEST_DATA.get(test_type,''):

                name, data, expected = case
                self.assert_message = f'\n CASE: {name} in {self.__module__}.{self._testMethodName}'

                func(self, data, expected)

            return 

        return wrapper