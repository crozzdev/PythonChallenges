from anagram_checker import are_anagrams


def test_are_anagrams_case_1():
    assert are_anagrams("listen", "silent")


def test_are_anagrams_case_2():
    assert are_anagrams("School master", "The classroom")


def test_are_anagrams_case_3():
    assert are_anagrams("A gentleman", "Elegant man")


def test_are_anagrams_case_4():
    assert not are_anagrams("Hello", "World")


def test_are_anagrams_case_5():
    assert not are_anagrams("apple", "banana")


def test_are_anagrams_case_6():
    assert not are_anagrams("cat", "dog")


def test_are_anagramas_case_7():
    assert not are_anagrams("aab", "bba")
