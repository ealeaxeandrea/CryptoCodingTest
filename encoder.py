# Функція для шифрування за допомогою алгоритму Цезаря
def caesar_encode(text: str, shift: int = 3) -> str:
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Функція для декодування тексту за допомогою алгоритму Цезаря
def caesar_decode(text: str, shift: int = 3) -> str:
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Функція для інверсії бітів у бінарному рядку
def bit_invert(binary_string: str) -> str:
    return ''.join('1' if bit == '0' else '0' for bit in binary_string if bit in '01')

# Функція для перевірки коректності бітового рядка
def is_valid_binary(binary_string: str) -> bool:
    return all(bit in '01' for bit in binary_string)
