from word_search import find_word
import pytest


@pytest.mark.parametrize(
    "matrix, word, expected",
    [
        ([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat", [[0, 1], [2, 1]]),
        ([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog", [[0, 0], [0, 2]]),
        (
            [
                ["h", "i", "s", "h"],
                ["i", "s", "f", "s"],
                ["f", "s", "i", "i"],
                ["s", "h", "i", "f"],
            ],
            "fish",
            [[3, 3], [0, 3]],
        ),
        (
            [
                ["f", "x", "o", "x"],
                ["o", "x", "o", "f"],
                ["f", "o", "f", "x"],
                ["f", "x", "x", "o"],
            ],
            "fox",
            [[1, 3], [1, 1]],
        ),
    ],
)
def test_find_word(matrix, word, expected):
    assert find_word(matrix, word) == expected
