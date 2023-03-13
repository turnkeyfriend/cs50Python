from twttr import shorten

def test_shorten():
    assert shorten("Mommy") == "Mmmy"
    assert shorten("supercalifragilisticexpialidotious") == "sprclfrglstcxpldts"
    assert shorten("Apple") == "ppl"
    assert shorten("1337 speak") == "1337 spk"
    assert shorten("This.is.the.time.") == "Ths.s.th.tm."
