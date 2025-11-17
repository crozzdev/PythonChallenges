import pytest
from matrix_builder import build_matrix


@pytest.mark.parametrize(
    "rows, cols, expected",
    [
        (2, 3, [[0, 0, 0], [0, 0, 0]]),
        (3, 2, [[0, 0], [0, 0], [0, 0]]),
        (4, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        (9, 1, [[0], [0], [0], [0], [0], [0], [0], [0], [0]]),
    ],
)
def test_build_matrix(rows, cols, expected):
    assert build_matrix(rows, cols) == expected
