def find_word(matrix: list[list[str]], word: str) -> list[list[int]] | None:
    """
    Find a word in a 2D matrix and return start and end coordinates.

    Args:
        matrix: 2D list of single lowercase letters
        word: Word to find in the matrix

    Returns:
        [[start_row, start_col], [end_row, end_col]] or None if not found
    """
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    word_size = len(word)

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == word[0]:
                positions_right, positions_left, positions_up, positions_down = [
                    [[i, j]] for _ in range(4)
                ]

                for k in range(1, word_size):
                    # we look to the right
                    # do we have enough cells to the right?
                    if j <= n_columns - word_size and matrix[i][j + k] == word[k]:
                        positions_right.append([i, j + k])
                        if len(positions_right) == word_size:
                            return [positions_right[0], positions_right[-1]]

                    # we look to the left
                    # do we have enough cells to the left?
                    if j >= word_size - 1 and matrix[i][j - k] == word[k]:
                        positions_left.append([i, j - k])
                        if len(positions_left) == word_size:
                            return [positions_left[0], positions_left[-1]]

                    # we look down
                    # do we have enough cells downwards?
                    if i <= n_rows - word_size and matrix[i + k][j] == word[k]:
                        positions_down.append([i + k, j])
                        if len(positions_down) == word_size:
                            return [positions_down[0], positions_down[-1]]

                    # we look up
                    # do we have enough cells upwards?
                    if i >= word_size - 1 and matrix[i - k][j] == word[k]:
                        positions_up.append([i - k, j])
                        if len(positions_up) == word_size:
                            return [positions_up[0], positions_up[-1]]


print(find_word([["g", "o", "d"], ["o", "g", "d"], ["d", "g", "o"]], "dog"))

print(
    find_word(
        [
            ["h", "i", "s", "h"],
            ["i", "s", "f", "s"],
            ["f", "s", "i", "i"],
            ["s", "h", "i", "f"],
        ],
        "fish",
    )
)
