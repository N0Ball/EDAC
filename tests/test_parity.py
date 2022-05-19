import unittest

from tests.testbase import TestBase

from modules.edac.methods.parity import Parity


class TestDecodeParity(TestBase):

    PARITY = Parity()

    @TestBase.parameterized
    def test_encode(self, data, expected):
        
        parity = self.PARITY.encode(data)
        
        self.assertEqual(parity, expected, self.assert_message)

    @TestBase.parameterized
    def test_decode(self, data, expected):

        msg, parity = tuple(data)
        expect_pass, expect_data, expect_error_bits = tuple(expected)

        is_pass, original_data, error_bits = self.PARITY.decode(msg, parity)

        self.assertEqual(is_pass, expect_pass, self.assert_message)
        self.assertEqual(original_data, expect_data, self.assert_message)
        self.assertEqual(error_bits, expect_error_bits, self.assert_message)

if __name__ == '__main__':
    unittest.main()