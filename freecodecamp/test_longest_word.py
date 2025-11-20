from longest_word import longest_word
import pytest


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("The quick red fox", "quick"),
        ("Hello coding challenge.", "challenge"),
        ("Do Try This At Home.", "This"),
        (
            "This sentence... has commas, ellipses, and an exlamation point!",
            "exlamation",
        ),
        ("A tie? No way!", "tie"),
        ("Wouldn't you like to know.", "Wouldnt"),
    ],
)
def test_longest_word(sentence, expected):
    assert longest_word(sentence) == expected
