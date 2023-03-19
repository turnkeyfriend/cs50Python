from numb3rs import validate

def test_letters():
    assert validate("my.mom.loves.food") == False

def test_lotta_dots():
    assert validate("..123...453...2.3.4...") == False

def test_small():
    assert validate("1.2.3.4") == True

def test_firstinrange():
    assert validate("25.344.433.256") == False
