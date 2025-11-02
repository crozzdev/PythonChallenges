def max_count(banned: list[int], n: int, max_sum: int) -> int:
    seen_numbers = []

    for i in range(1, n + 1):
        if i not in banned and i not in seen_numbers:
            if sum(seen_numbers) + i <= max_sum:
                seen_numbers.append(i)

    return len(seen_numbers)


print(max_count([3], 5, 4))
