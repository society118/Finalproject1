def shift_words(text: str, shift: int) -> str:
    def shift_char(c):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base + shift) % 26 + base)
        return c

    return ''.join(shift_char(c) for c in text)


if __name__ == '__main__':
    test_string = "hello world"
    shifted = shift_words(test_string, 2)
    print(f"Оригінал: '{test_string}'")
    print(f"Результат: '{shifted}'")
