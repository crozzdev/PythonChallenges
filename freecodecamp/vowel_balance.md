# Vowel balance challenge


## Instructions

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.

## Test cases

1. is_balanced("racecar") should return True.
2. is_balanced("Lorem Ipsum") should return True.
3. is_balanced("Kitty Ipsum") should return False.
4. is_balanced("string") should return False.
5. is_balanced(" ") should return True.
6. is_balanced("abcdefghijklmnopqrstuvwxyz") should return False.
7. is_balanced("123A#b!E&*456-o.U") should return True.