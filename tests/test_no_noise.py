import unittest

from tests.testbase import TestBase

from modules.noise.nonoise import NoNoise
from modules import Debug

class TestNoNoise(TestBase):

    NO_NOISE = NoNoise()

    @TestBase.parameterized
    def test_default(self, data, expected):

        result = self.NO_NOISE.add_noise(data)

        self.assertEqual(result, expected, self.assert_message)

    @TestBase.parameterized
    def test_invalid(self, data, expected):

        with self.assertRaises(ValueError) as context:
            self.NO_NOISE.add_noise(str(data))

        self.assertEqual(str(context.exception), expected, self.assert_message)

if __name__ == '__main__':

    unittest.main()