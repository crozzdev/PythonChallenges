# Base check challenge

## Instructions

Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z

## Test cases

1. is_valid_number("10101", 2) should return True.
2. is_valid_number("10201", 2) should return False.
3. is_valid_number("76543210", 8) should return True.
4. is_valid_number("9876543210", 8) should return False.
5. is_valid_number("9876543210", 10) should return True.
6. is_valid_number("ABC", 10) should return False.
7. is_valid_number("ABC", 16) should return True.
8. is_valid_number("10101", 2) should return True.
9. is_valid_number("ABC", 20) should return True.
10. is_valid_number("4B4BA9", 16) should return True.
11. is_valid_number("5G3F8F", 16) should return False.
12. is_valid_number("5G3F8F", 17) should return True.
13. is_valid_number("abc", 10) should return False.
14. is_valid_number("abc", 16) should return True.
15. is_valid_number("AbC", 16) should return True.
16. is_valid_number("z", 36) should return True.