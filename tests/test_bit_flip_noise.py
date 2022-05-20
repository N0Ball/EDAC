import unittest
from Crypto.Util.number import long_to_bytes, bytes_to_long

from tests.testbase import TestBase

from modules.noise.methods.bitflip import BitFlipNoise

# TODO since this class doesn't constructed well, therefore the futher
# test data will be done later
class TestBitFlipNoise(TestBase):

    # TODO give a default debug value to this
    BIT_FLIP = BitFlipNoise(True, flip_list=[])

    @TestBase.parameterized
    def test_random(self, data, expected):

        data = long_to_bytes(data)
        result = self.BIT_FLIP.add_noise(data)
        
        data = bin(bytes_to_long(data))
        result = bin(bytes_to_long(result))

        diff = [i for i in range(len(data)) if data[i] != result[i]]
        
        self.assertEqual(len(diff), expected, self.assert_message)
        