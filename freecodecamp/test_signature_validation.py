from signature_validation import verify


def test_verify_case_1():
    assert verify("foo", "bar", 57)


def test_verify_case_2():
    assert not verify("foo", "bar", 54)


def test_verify_case_3():
    assert verify("freeCodeCamp", "Rocks", 238)


def test_verify_case_4():
    assert not verify("Is this valid?", "No", 210)


def test_verify_case_5():
    assert verify("Is this valid?", "Yes", 233)


def test_verify_case_6():
    assert verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514)
