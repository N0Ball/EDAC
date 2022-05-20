import unittest
from Crypto.Util.number import long_to_bytes, bytes_to_long

from tests.testbase import TestBase

from modules.noise.methods.bitflip import BitFlipNoise

# TODO since this class doesn't constructed well, therefore the futher
# test data will be done later
class TestBitFlipNoise(TestBase):

    # TODO give a default debug value to this
    BIT_FLIP = BitFlipNoise(False, flip_list=[])
    ITERATE_TIME = 1000

    @TestBase.parameterized
    def test_random(self, data, expected):

        for _ in range(self.ITERATE_TIME):
            data = long_to_bytes(data)
            result = self.BIT_FLIP.add_noise(data)
            
            data = bytes_to_long(data)
            result = bytes_to_long(result)

            diff = sum(map(int, bin(data ^ result)[2:]))
            
            self.assertEqual(diff, expected, self.assert_message)

if __name__ == '__main__':
    unittest.main()