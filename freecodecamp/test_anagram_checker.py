from anagram_checker import are_anagrams

def test_are_anagrams_case_1():
    assert are_anagrams("listen", "silent") == True

def test_are_anagrams_case_2():
    assert are_anagrams("School master", "The classroom") == True

def test_are_anagrams_case_3():
    assert are_anagrams("A gentleman", "Elegant man") == True

def test_are_anagrams_case_4():
    assert are_anagrams("Hello", "World") == False

def test_are_anagrams_case_5():
    assert are_anagrams("apple", "banana") == False

def test_are_anagrams_case_6():
    assert are_anagrams("cat", "dog") == False
  
def test_are_anagramas_case_7():
    assert are_anagrams("aab", "bba") == False