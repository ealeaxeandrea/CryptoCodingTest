import unittest
from encoder import caesar_encode, bit_invert

class TestEncoder(unittest.TestCase):

    def test_caesar_encode_basic(self):
        self.assertEqual(caesar_encode("abc"), "def")

    def test_caesar_encode_mixed(self):
        self.assertEqual(caesar_encode("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_bit_invert_simple(self):
        self.assertEqual(bit_invert("1010"), "0101")

    def test_bit_invert_with_noise(self):
        self.assertEqual(bit_invert("10x1 01"), "01")

if __name__ == '__main__':
    unittest.main()
