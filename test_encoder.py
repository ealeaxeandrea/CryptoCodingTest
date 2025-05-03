import unittest
from encoder import caesar_encode, caesar_decode, bit_invert, is_valid_binary

class TestEncoder(unittest.TestCase):

    # Тест для шифрування за допомогою алгоритму Цезаря
    def test_caesar_encode_basic(self):
        self.assertEqual(caesar_encode("abc"), "def")

    # Тест для декодування за допомогою алгоритму Цезаря
    def test_caesar_decode_basic(self):
        self.assertEqual(caesar_decode("def"), "abc")

    # Тест для інверсії бітів у рядку
    def test_bit_invert_simple(self):
        self.assertEqual(bit_invert("1010"), "0101")

    # Тест для перевірки коректності бінарного рядка
    def test_is_valid_binary(self):
        self.assertTrue(is_valid_binary("10101"))
        self.assertFalse(is_valid_binary("10201"))

if __name__ == '__main__':
    unittest.main()
