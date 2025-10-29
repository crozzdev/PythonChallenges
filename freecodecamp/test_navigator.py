from navigator import navigate

def test_navigate_case_1():
    assert navigate(["Visit About Us", "Back", "Forward"]) == "About Us"

def test_navigate_case_2():
    assert navigate(["Forward"]) == "Home"

def test_navigate_case_3():
    assert navigate(["Back"]) == "Home"

def test_navigate_case_4():
    assert navigate(["Visit About Us", "Visit Gallery"]) == "Gallery"

def test_navigate_case_5():
    assert navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) == "Home"

def test_navigate_case_6():
    assert navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) == "Contact"

def test_navigate_case_7():
    assert navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) == "Visit Us"
