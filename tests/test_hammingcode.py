import unittest
from Crypto.Util.number import bytes_to_long, long_to_bytes

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

    @TestBase.parameterized
    def test_default_decode(self, data, expected):

        is_pass, decoded_data, error_bits = self.HAMMING_CODE.decode(long_to_bytes(data))

        expected_pass, expected_data, expected_errors = tuple(expected)
        expected_data = expected_data.encode('utf8')
        
        self.assertEqual(is_pass, expected_pass, self.assert_message)
        self.assertEqual(decoded_data, expected_data, self.assert_message)
        self.assertEqual(error_bits, expected_errors, self.assert_message)

if __name__ == '__main__':

    unittest.main()