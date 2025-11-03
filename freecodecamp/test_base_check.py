from base_check import is_valid_number


def test_case_1_base2_valid():
    assert is_valid_number("10101", 2) is True


def test_case_2_base2_invalid():
    assert is_valid_number("10201", 2) is False


def test_case_3_base8_valid():
    assert is_valid_number("76543210", 8) is True


def test_case_4_base8_invalid():
    assert is_valid_number("9876543210", 8) is False


def test_case_5_base10_valid():
    assert is_valid_number("9876543210", 10) is True


def test_case_6_base10_alpha_invalid():
    assert is_valid_number("ABC", 10) is False


def test_case_7_base16_alpha_valid():
    assert is_valid_number("ABC", 16) is True


def test_case_8_duplicate_base2_valid():
    # Duplicate of case 1 per spec
    assert is_valid_number("10101", 2) is True


def test_case_9_base20_alpha_valid():
    assert is_valid_number("ABC", 20) is True


def test_case_10_base16_mixed_valid():
    assert is_valid_number("4B4BA9", 16) is True


def test_case_11_base16_contains_g_invalid():
    assert is_valid_number("5G3F8F", 16) is False


def test_case_12_base17_g_allowed():
    assert is_valid_number("5G3F8F", 17) is True


def test_case_13_lowercase_abc_base10_invalid():
    assert is_valid_number("abc", 10) is False


def test_case_14_lowercase_abc_base16_valid():
    assert is_valid_number("abc", 16) is True


def test_case_15_mixedcase_AbC_base16_valid():
    assert is_valid_number("AbC", 16) is True


def test_case_16_z_base36_valid():
    assert is_valid_number("z", 36) is True
