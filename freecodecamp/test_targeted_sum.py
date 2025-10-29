from targeted_sum import find_target

def test_find_target_case_1():
    assert find_target([2, 7, 11, 15], 9) == [0,1]

def test_find_target_case_2():
    assert find_target([3, 2, 4, 5], 6) == [1,2]

def test_find_target_case_3():
    assert find_target([1, 3, 5, 6, 7, 8], 15) == [4,5]

def test_find_target_case_4():
    assert find_target([1, 3, 5, 7], 14) == "Target not found"