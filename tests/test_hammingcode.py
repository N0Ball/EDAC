from multiprocessing.sharedctypes import Value
import unittest
from Crypto.Util.number import long_to_bytes

from tests.testbase import TestBase

from modules.edac import HammingCode

class TestHammingCode(TestBase):

    HAMMING_CODE = HammingCode()

    @TestBase.parameterized
    def test_default_encode(self, data, expected):

        target = 0
        if data != 0:
            for e in data.encode('utf8'):
                
                target <<= 8
                target += e

        result = self.HAMMING_CODE.encode(target)

        self.assertEqual(result, expected, self.assert_message + 
            f'{bin(result) = } but {bin(expected) = }'
        )

    @TestBase.parameterized
    def test_default_decode(self, data, expected):

        is_pass, decoded_data, error_bits = self.HAMMING_CODE.decode(data)

        decoded_data = long_to_bytes(decoded_data)
        
        self.assertEqual(is_pass, expected.get('is_pass'), self.assert_message)
        self.assertEqual(decoded_data, expected.get('decoded').encode('utf8'), self.assert_message)
        self.assertEqual(error_bits, expected.get('error_bits'), self.assert_message)

    def test_iter_all(self):

        encoded_message = list(map(int, '1010000011000110'))

        for i in range(15):
            encoded_message[i] = int(not encoded_message[i])

            message = int(''.join(map(str, encoded_message)), 2)
            is_pass, decoded_data, error_bits = self.HAMMING_CODE.decode(message)
            decoded_data = chr(decoded_data)

            self.assertEqual(is_pass, True)
            self.assertEqual(decoded_data, 'F')
            self.assertEqual(error_bits, [i])

            encoded_message[i] = int(not encoded_message[i])

    @TestBase.parameterized
    def test_custom_encode(self, data, expected):

        self.HAMMING_CODE = HammingCode(data.get('size'))

        target = 0
        if data.get('input') != 0:
            for e in data.get('input').encode('utf8'):
                
                target <<= 8
                target += e

        result = self.HAMMING_CODE.encode(target)

        self.assertEqual(result, expected, self.assert_message + 
            f'{bin(result) = } but {bin(expected) = }'
        )

    @TestBase.parameterized
    def test_custom_decode(self, data, expected):

        self.HAMMING_CODE = HammingCode(data.get('size'))

        is_pass, decoded_data, error_bits = self.HAMMING_CODE.decode(data.get('input'))

        decoded_data = long_to_bytes(decoded_data)
        
        self.assertEqual(is_pass, expected.get('is_pass'), self.assert_message)
        self.assertEqual(decoded_data, expected.get('decoded').encode('utf8'), self.assert_message)
        self.assertEqual(error_bits, expected.get('error_bits'), self.assert_message)


    @TestBase.parameterized
    def test_invalid_input(self, data, expected):

        with self.assertRaises(ValueError) as context:
            self.HAMMING_CODE = HammingCode(data)
            self.HAMMING_CODE.encode(1)

        self.assertEqual(str(context.exception), expected, self.assert_message)


if __name__ == '__main__':

    unittest.main()