from pytest import raises

from fuel import convert
from fuel import gauge

def test_reg_fract():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_zero_denom():
    with raises(ZeroDivisionError):
        convert("4/0")

def test_fract_numer():
    with raises(ValueError):
        convert("three/four")
    with raises(ValueError):
        convert("1.5/3")

def test_full():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
