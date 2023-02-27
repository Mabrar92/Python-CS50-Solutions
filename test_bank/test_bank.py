from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello, newman") == 0

def test_case():
    assert value("Hello") == 0

def test_hi():
    assert value("hi") == 20
    assert value("hola") == 20

def test_other():
    assert value("Good Morning") == 100

def test_numbers():
    assert value("123") == 100