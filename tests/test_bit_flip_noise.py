from math import ceil
import unittest

from tests.testbase import TestBase

from modules.noise import BitFlip

class TestBitFlip(TestBase):

    BIT_FLIP = BitFlip()
    ITERATE_TIME = 1000

    @TestBase.parameterized
    def test_random(self, data, expected):

        for _ in range(self.ITERATE_TIME):

            result = self.BIT_FLIP.add_noise(data)

            diff = sum(map(int, bin(data ^ result)[2:].rjust(8, '0')))
            
            self.assertEqual(diff, expected, self.assert_message)

    @TestBase.parameterized
    def test_flip_list(self, data, expected):

        target = data.get('input')
        flip_list = data.get('flip_list')

        self.BIT_FLIP = BitFlip(flip_list)
        result = self.BIT_FLIP.add_noise(target)

        LEN = len(bin(target)[2:])

        diff_index = [x[0] for x in filter(lambda x: x[1] == 1, enumerate((map(int, bin(target^result)[2:].rjust(LEN, '0')))))]
        diff_num = len(diff_index)

        self.assertEqual(diff_num, expected.get('diff'), self.assert_message)
        self.assertEqual(diff_index, expected.get('flipped'), self.assert_message)

    @TestBase.parameterized
    def test_invalid(self, data, expected):

        with self.assertRaises(ValueError) as context:
            self.BIT_FLIP.add_noise(str(data))

        self.assertEqual(str(context.exception), expected, self.assert_message)

    @TestBase.parameterized
    def test_index_exceed(self, data, expected):

        with self.assertRaises(IndexError) as context:
            self.BIT_FLIP = BitFlip(data.get('flip_list'))
            self.BIT_FLIP.add_noise(data.get('input'))

        self.assertEqual(str(context.exception), expected, self.assert_message)


if __name__ == '__main__':
    unittest.main()