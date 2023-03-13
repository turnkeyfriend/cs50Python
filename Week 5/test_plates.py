from plates import is_valid

def test_alnum():
    assert is_valid("PI3!14") == False
    #assert is_valid("PI3*14") == False
    #assert is_valid("PI3@14") == False
    #assert is_valid("PI3.14") == False

def test_length():
    assert is_valid("a") == False
    #assert is_valid("b") == False
    #assert is_valid("abcdefghijk") == False
    #assert is_valid("asdjflksjdhflksdjh") == False

def test_zero_place():
    #assert is_valid("0badde") == False
    #assert is_valid("0dsasd") == False
    #assert is_valid("0hgiee") == False
    assert is_valid("CS0456") == False
    #assert is_valid("CS50") == True

def test_num_place():
    assert is_valid("CS50P") == False
    #assert is_valid("CS50L") == False
    #assert is_valid("CS507H") == False
    #assert is_valid("cs432m") == False

def test_alpha_begin():
    assert is_valid("323420") == False
    assert is_valid("14span") == False
    assert is_valid("42hght") == False
    assert is_valid("1dom") == False
