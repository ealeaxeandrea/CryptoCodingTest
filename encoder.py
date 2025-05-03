def caesar_encode(text: str, shift: int = 3) -> str:
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decode(text: str, shift: int = 3) -> str:
    return caesar_encode(text, -shift)

def bit_invert(binary_string: str) -> str:
    # Фільтруємо тільки символи '0' або '1'
    clean_string = ''.join(filter(lambda x: x in '01', binary_string))
    # Інвертуємо біт
    return ''.join('1' if bit == '0' else '0' for bit in clean_string)






def is_valid_binary(s: str) -> bool:
    return all(c in '01' for c in s)
