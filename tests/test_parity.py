import unittest
from Crypto.Util.number import long_to_bytes, bytes_to_long

from tests.testbase import TestBase

from modules.edac.parity import Parity

class TestDecodeParity(TestBase):

    PARITY = Parity()

    @TestBase.parameterized
    def test_default_encode(self, data, expected):
        
        result = bytes_to_long(self.PARITY.encode(long_to_bytes(data)))
        
        self.assertEqual(result, expected, self.assert_message)

    @TestBase.parameterized
    def test_custom_encode(self, data, expected):

        result = bytes_to_long(self.PARITY.encode(long_to_bytes(data.get('input')), n=data.get('size')))

        self.assertEqual(result, expected, self.assert_message)


    @TestBase.parameterized
    def test_default_decode(self, data, expected):

        expected_pass = expected.get('pass')
        expected_decoded = expected.get('decoded')
        expected_error_bits = expected.get('error_bits')

        is_pass, original_data, error_bits = self.PARITY.decode(long_to_bytes(data))
        original_data = bytes_to_long(original_data)

        self.assertEqual(is_pass, expected_pass, self.assert_message)
        self.assertEqual(original_data, expected_decoded, self.assert_message)
        self.assertEqual(error_bits, expected_error_bits, self.assert_message)

    @TestBase.parameterized
    def test_custom_decode(self, data, expected):

        is_pass, original_data, error_bits = self.PARITY.decode(
            long_to_bytes(data.get('input')),
            n=data.get('size')
        )

        original_data = bytes_to_long(original_data)

        self.assertEqual(
            is_pass, expected.get('pass'), self.assert_message
        )

        self.assertEqual(
            original_data, expected.get('decoded'), self.assert_message
        )

        self.assertEqual(
            error_bits, expected.get('error_bits'), self.assert_message
        )

if __name__ == '__main__':
    unittest.main()