def find_word(matrix: list[list[str]], word: str) -> list[list[int]] | None:
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    word_size = len(word)
    word_list = list(word)

    corners = {
        "upper-left": (0, 0),
        "upper-right": (0, n_rows - 1),
        "bottom-left": (n_columns - 1, 0),
        "bottom-right": (n_columns - 1, n_rows - 1),
    }

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            cell_pos = (i, j)

            if cell == word[0]:
                seen_right, seen_left, seen_up, seen_down = [[cell] for _ in range(4)]
                positions_right, positions_left, positions_up, positions_down = [
                    [[i, j]] for _ in range(4)
                ]

                for k in range(1, word_size):
                    # we look to the right
                    # do we have enough cells to the right?
                    if (
                        cell_pos
                        not in [corners["bottom-right"], corners["upper-right"]]
                        and j <= n_columns - word_size
                        and matrix[i][j + k] == word[k]
                    ):
                        positions_right.append([i, j + k])
                        seen_right.append(matrix[i][j + k])
                        if seen_right == word_list:
                            return [positions_right[0], positions_right[-1]]

                    # we look to the left
                    # do we have enough cells to the left?
                    if (
                        cell_pos not in [corners["bottom-left"], corners["upper-left"]]
                        and j >= word_size - 1
                        and matrix[i][j - k] == word[k]
                    ):
                        positions_left.append([i, j - k])
                        seen_left.append(matrix[i][j - k])
                        if seen_left == word_list:
                            return [positions_left[0], positions_left[-1]]

                    # we look down
                    # do we have enough cells downwards?
                    if (
                        cell_pos
                        not in [corners["bottom-left"], corners["bottom-right"]]
                        and i <= n_rows - word_size
                        and matrix[i + k][j] == word[k]
                    ):
                        positions_down.append([i + k, j])
                        seen_down.append(matrix[i + k][j])
                        if seen_down == word_list:
                            return [positions_down[0], positions_down[-1]]

                    # we look up
                    # do we have enough cells upwards?
                    if (
                        cell_pos not in [corners["upper-left"], corners["upper-right"]]
                        and i >= word_size - 1
                        and matrix[i - k][j] == word[k]
                    ):
                        positions_up.append([i - k, j])
                        seen_up.append(matrix[i - k][j])
                        if seen_up == word_list:
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
