from working import convert
import pytest

def test_middle():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_minutes():
    with pytest.raises(ValueError):
        convert("12:60 AM to 1:05 PM")

def test_something():
    assert convert("11:00 AM to 2:00 PM") == "11:00 to 14:00"
