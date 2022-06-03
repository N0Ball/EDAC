import unittest

from tests.testbase import TestBase

from modules.edac.parity import Parity

class TestDecodeParity(TestBase):

    PARITY = Parity()

    @TestBase.parameterized
    def test_default_encode(self, data, expected):
        
        result = self.PARITY.encode(data)
        
        self.assertEqual(result, expected, self.assert_message)

    @TestBase.parameterized
    def test_custom_encode(self, data, expected):

        result = self.PARITY.encode(data.get('input'), n=data.get('size'))

        self.assertEqual(result, expected, self.assert_message)


    @TestBase.parameterized
    def test_default_decode(self, data, expected):

        expected_pass = expected.get('pass')
        expected_decoded = expected.get('decoded')
        expected_error_bits = expected.get('error_bits')

        is_pass, decoded, error_bits = self.PARITY.decode(data)

        self.assertEqual(is_pass, expected_pass, self.assert_message)
        self.assertEqual(decoded, expected_decoded, self.assert_message)
        self.assertEqual(error_bits, expected_error_bits, self.assert_message)

    @TestBase.parameterized
    def test_custom_decode(self, data, expected):

        is_pass, decoded, error_bits = self.PARITY.decode(
            data.get('input'),
            n=data.get('size')
        )

        self.assertEqual(
            is_pass, expected.get('pass'), self.assert_message
        )

        self.assertEqual(
            decoded, expected.get('decoded'), self.assert_message
        )

        self.assertEqual(
            error_bits, expected.get('error_bits'), self.assert_message
        )

if __name__ == '__main__':
    unittest.main()