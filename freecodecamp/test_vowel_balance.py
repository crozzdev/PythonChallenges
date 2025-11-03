from vowel_balance import is_balanced


def test_vowel_balance_cases():
    assert is_balanced("racecar")
    assert is_balanced("Lorem Ipsum")
    assert not is_balanced("Kitty Ipsum")
    assert not is_balanced("string")


def test_vowel_balance_edge_cases():
    assert is_balanced(" ")
    assert not is_balanced("abcdefghijklmnopqrstuvwxyz")
    assert is_balanced("123A#b!E&*456-o.U")
