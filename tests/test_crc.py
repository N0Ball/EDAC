import unittest
from Crypto.Util.number import bytes_to_long, long_to_bytes

from tests.testbase import TestBase

from modules.edac import CRC
from modules.edac.methodschema.crc import SCHEMA, GENERATOR

class TestDecodeParity(TestBase):

    CRC = CRC()

    @TestBase.parameterized
    def test_default_encode(self, data, expected):

        target = bytes_to_long(data.encode('utf8'))

        result = self.CRC.encode(target)

        self.assertEqual(result, expected, self.assert_message + 
            f'The result should be {bin(expected) = }, but {bin(result) = } recieved'
        )

    @TestBase.parameterized
    def test_default_decode(self, data, expected):

        is_pass, decoded, error_bits = self.CRC.decode(data)

        self.assertEqual(is_pass, expected.get('is_pass'), self.assert_message)
        self.assertEqual(long_to_bytes(decoded), expected.get('decoded').encode('utf8'), self.assert_message)
        self.assertEqual(error_bits, expected.get('error_bits'), self.assert_message)

    @TestBase.parameterized
    def test_custom_encode(self, data, expected):

        self.CRC = CRC(data.get('size'))
        target = bytes_to_long(data.get('input').encode('utf8'))

        result = self.CRC.encode(target)

        self.assertEqual(result, expected, self.assert_message + 
            f'The result should be {bin(expected) = }, but {bin(result) = } recieved'
        )

    @TestBase.parameterized
    def test_custom_decode(self, data, expected):

        self.CRC = CRC(data.get('size'))
        
        is_pass, decoded, error_bits = self.CRC.decode(data.get('input'))

        self.assertEqual(is_pass, expected.get('is_pass'), self.assert_message)
        self.assertEqual(long_to_bytes(decoded), expected.get('decoded').encode('utf8'), self.assert_message)
        self.assertEqual(error_bits, expected.get('error_bits'), self.assert_message)


    @TestBase.parameterized
    def test_custom_schema_encode(self, data, expected):

        self.CRC = CRC(block_size=data.get('size'), type=SCHEMA.CRC_16_CCITT)
        target = bytes_to_long(data.get('input').encode('utf8'))

        result = self.CRC.encode(target)

        self.assertEqual(result, expected, self.assert_message + 
            f'The result should be \n\t{bin(expected)}, but \n\t{bin(result)} recieved'
        )

    @TestBase.parameterized
    def test_custom_schema_decode(self, data, expected):

        self.CRC = CRC(data.get('size'), type=SCHEMA.CRC_16_CCITT)
        is_pass, decoded, error_bits = self.CRC.decode(data.get('input'))

        self.assertEqual(is_pass, expected.get('is_pass'), self.assert_message)
        self.assertEqual(long_to_bytes(decoded), expected.get('decoded').encode('utf8'), self.assert_message)
        self.assertEqual(error_bits, expected.get('error_bits'), self.assert_message)

if __name__ == '__main__':
    unittest.main()