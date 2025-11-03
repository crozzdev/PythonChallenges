from nth_prime import nth_prime


def test_nth_prime_case_1():
    assert nth_prime(5) == 11


def test_nth_prime_case_2():
    assert nth_prime(10) == 29


def test_nth_prime_case_3():
    assert nth_prime(16) == 53


def test_nth_prime_case_4():
    assert nth_prime(99) == 523


def test_nth_prime_case_5():
    assert nth_prime(1000) == 7919
