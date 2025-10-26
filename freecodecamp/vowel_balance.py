VOWELS = ["a","e","i","o","u"]

def is_balanced(s:str) -> bool:
    length_s = len(s)
    center = length_s // 2
    s_copy = s.lower()
    left = [vowel for vowel in s_copy[:center] if vowel in VOWELS]
    if length_s % 2 == 0:
        
        right = [vowel for vowel in s_copy[center:] if vowel in VOWELS]
    else:
        right = [vowel for vowel in s_copy[center+1:] if vowel in VOWELS]

    return len(left) == len(right)
    
