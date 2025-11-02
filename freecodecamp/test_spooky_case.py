from spooky_case import spookify


def test_spookify_case_1():
    assert spookify("hello_world") == "HeLlO~wOrLd"


def test_spookify_case_2():
    assert spookify("Spooky_Case") == "SpOoKy~CaSe"


def test_spookify_case_3():
    assert spookify("TRICK-or-TREAT") == "TrIcK~oR~tReAt"


def test_spookify_case_4():
    assert spookify("c_a-n_d-y_-b-o_w_l") == "C~a~N~d~Y~~b~O~w~L"


def test_spookify_case_5():
    assert (
        spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts")
        == "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS"
    )
