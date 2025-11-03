from email_sorter import sort


def test_sort_case_1():
    assert sort(["jill@mail.com", "john@example.com", "jane@example.com"]) == [
        "jane@example.com",
        "john@example.com",
        "jill@mail.com",
    ]


def test_sort_case_2():
    assert sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]) == [
        "bob@mail.com",
        "carol@mail.com",
        "alice@zoo.com",
    ]


def test_sort_case_3():
    assert sort(["user@z.com", "user@y.com", "user@x.com"]) == [
        "user@x.com",
        "user@y.com",
        "user@z.com",
    ]


def test_sort_case_4():
    assert sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]) == [
        "amy@mail.COM",
        "bob@Mail.com",
        "sam@MAIL.com",
    ]


def test_sort_case_5():
    assert sort(
        [
            "simon@beta.com",
            "sammy@alpha.com",
            "Sarah@Alpha.com",
            "SAM@ALPHA.com",
            "Simone@Beta.com",
            "sara@alpha.com",
        ]
    ) == [
        "SAM@ALPHA.com",
        "sammy@alpha.com",
        "sara@alpha.com",
        "Sarah@Alpha.com",
        "simon@beta.com",
        "Simone@Beta.com",
    ]
