import unittest

from tests.testbase import TestBase

class TestGetTestData(TestBase):

    @TestBase.parameterized
    def test_get_data(self, data, expected):

        target = data[0]
        expected_value = expected[0]
        
        self.assertEqual(target, expected_value, self.assert_message)

if __name__ == '__main__':
    unittest.main()