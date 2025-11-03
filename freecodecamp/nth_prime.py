def is_prime(number: int) -> bool:
    factors = 0
    for n in range(1, number + 1):
        if number % n == 0:
            factors += 1
        if factors > 2:
            return False
    return True


def nth_prime(n: int) -> int | None:
    total_primes = 0
    counter = 2

    while total_primes < n:
        if is_prime(counter):
            total_primes += 1
            if total_primes == n:
                return counter
        counter += 1
