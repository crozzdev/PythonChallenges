from vowel_balance import is_balanced

def test_vowel_balance_cases():
    assert is_balanced("racecar") == True
    assert is_balanced("Lorem Ipsum") == True
    assert is_balanced("Kitty Ipsum") == False
    assert is_balanced("string") == False

def test_vowel_balance_edge_cases():
    assert is_balanced(" ") == True
    assert is_balanced("abcdefghijklmnopqrstuvwxyz") == False
    assert is_balanced("123A#b!E&*456-o.U") == True