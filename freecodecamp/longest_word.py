import re


def longest_word(sentence: str) -> str:
    words = re.sub(r"[^A-Za-z\s]", "", sentence).split()

    max_word = ""
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word
