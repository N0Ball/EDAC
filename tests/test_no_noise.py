import unittest

from tests.testbase import TestBase

from modules.noise.methods.none import NoNoise

class TestNoNoise(TestBase):

    NO_NOISE = NoNoise(False)

    @TestBase.parameterized
    def test_default(self, data, expected):

        self.assertEqual(data, expected, self.assert_message)

if __name__ == '__main__':

    unittest.main()