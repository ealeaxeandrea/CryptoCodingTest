import unittest
from encoder import caesar_encode, caesar_decode, bit_invert, is_valid_binary
import time

class TestEncoder(unittest.TestCase):

    # Функціональні тести
    def test_caesar_encode_basic(self):
        self.assertEqual(caesar_encode("abc"), "def")

    def test_caesar_encode_mixed(self):
        self.assertEqual(caesar_encode("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_caesar_decode_basic(self):
        self.assertEqual(caesar_decode("def"), "abc")

    def test_bit_invert_simple(self):
        self.assertEqual(bit_invert("1010"), "0101")

    def test_bit_invert_with_noise(self):
    # Після очищення від "x" і пробілу залишиться "10101", який буде інвертовано в "01010"
        self.assertEqual(bit_invert("10x1 01"), "01010")



    def test_is_valid_binary_valid(self):
        self.assertTrue(is_valid_binary("10101"))

    def test_is_valid_binary_invalid(self):
        self.assertFalse(is_valid_binary("10201"))

    # Нефункціональні тести (перевірка часу виконання)
    def test_caesar_encode_performance(self):
        start_time = time.time()
        caesar_encode("A" * 1000000)  # Тестування на великому наборі даних
        end_time = time.time()
        self.assertTrue(end_time - start_time < 1, "Тестування на великому наборі даних займає забагато часу")

    def test_bit_invert_performance(self):
        start_time = time.time()
        bit_invert("1" * 1000000)  # Тестування на великому наборі даних
        end_time = time.time()
        self.assertTrue(end_time - start_time < 1, "Інверсія бітів займає забагато часу")

    # Тести на коректність обробки некоректних вхідних даних
    def test_caesar_encode_empty(self):
        self.assertEqual(caesar_encode(""), "")

    def test_bit_invert_empty(self):
        self.assertEqual(bit_invert(""), "")

if __name__ == '__main__':
    unittest.main()
