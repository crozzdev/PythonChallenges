def fibonacci_sequence(start_sequence:list, length:int) -> list:
    fibonacci_sequence = start_sequence
    if length <= 0:
        return []
    if length < len(fibonacci_sequence):
        return [fibonacci_sequence[length-1]]
    if length == len(fibonacci_sequence):
        return fibonacci_sequence

    for i in range(2,length):
        next_number = fibonacci_sequence[i-2] + fibonacci_sequence[i-1]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([123456789, 987654321], 5))
print(fibonacci_sequence([10, 20], 2))