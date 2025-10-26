
LETTERS_TO_NUMBERS= {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
    'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
    'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
    'Y': 34, 'Z': 35
}

def is_valid_number(s: str, base: int) -> bool:
    copy_s = s.upper()

    for char in copy_s:
        if char.isalpha():
            if char not in LETTERS_TO_NUMBERS or LETTERS_TO_NUMBERS[char] >= base:
                return False
            continue
        elif char.isdigit():
            if int(char) >= base:
                return False
        else:
            # Character is neither letter nor digit
            return False
    return True

print(is_valid_number("10101", 2))
print(is_valid_number("z", 36))
print(is_valid_number("5G3F8F", 16))
print(is_valid_number("abc", 10))

        