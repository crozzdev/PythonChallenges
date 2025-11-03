def fibonacci_sequence(start_sequence: list, length: int) -> list:
    if length <= 0:
        return []

    result = start_sequence.copy()

    if length <= len(result):
        return result[:length]

    for i in range(len(result), length):
        next_number = result[i - 2] + result[i - 1]
        result.append(next_number)

    return result


print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([123456789, 987654321], 5))
print(fibonacci_sequence([10, 20], 2))
