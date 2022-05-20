import unittest
from Crypto.Util.number import bytes_to_long

from tests.testbase import TestBase

from modules.edac.factory import EDACFactory
from modules.edac.schema import EDACType

class TestHammingCode(TestBase):

    HAMMING_CODE = EDACFactory(EDACType.HAMMING_CODE)

    @TestBase.parameterized
    def test_default_encode(self, data, expected):

        data = bytes.fromhex(data)

        result = bytes_to_long(self.HAMMING_CODE.encode(data))

        self.assertEqual(result, expected, self.assert_message + 
            f'{bin(result) = } but {bin(expected) = }'
        )
        


if __name__ == '__main__':

    unittest.main()