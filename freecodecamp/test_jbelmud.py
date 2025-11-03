from jbelmud import jbelmu


def test_case_1_jbelmu():
    assert jbelmu("hello world") == "hello wlord"


def test_case_2_jbelmu():
    assert jbelmu("i love jumbled text") == "i love jbelmud text"


def test_case_3_jbelmu():
    assert (
        jbelmu("freecodecamp is my favorite place to learn to code")
        == "faccdeeemorp is my faiortve pacle to laern to cdoe"
    )


def test_case_4_jbelmu():
    assert (
        jbelmu("the quick brown fox jumps over the lazy dog")
        == "the qciuk borwn fox jmpus oevr the lazy dog"
    )
