from twttr import shorten

def test_capital():
    assert shorten("BACEDIFOGU") == "BCDFG"

def test_small():
    assert shorten("bacedifogu") == "bcdfg"

def test_numbers():
    assert shorten("a1e234o") == "1234"

def test_punctuations():
    assert shorten(",b.ace:d'ifogu") == ",b.c:d'fg"