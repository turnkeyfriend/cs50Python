from bank import value

def test_bank():
    assert value("Hello") == 0

def test_2():
    assert value("Hiya") == 20

def test_3():
    assert value("My man") == 100

def test_bank_numeric():
    assert value("1234") == 100

def test_hello_more():
    assert value("heLLo to y0u") == 0
