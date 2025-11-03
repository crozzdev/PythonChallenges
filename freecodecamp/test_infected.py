from infected import infected


def test_infected_case_1():
    assert infected(1) == 2


def test_infected_case_2():
    assert infected(3) == 6


def test_infected_case_3():
    assert infected(8) == 152


def test_infected_case_4():
    assert infected(17) == 39808


def test_infected_case_5():
    assert infected(25) == 5217638
