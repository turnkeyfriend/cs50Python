import os
from project import cheese_one, cheese_two, cheese_three

def test_cheese_one():
    assert cheese_one() == "cheese_one passed"

def test_cheese_two():
    assert cheese_two() == "cheese_two passed"

def test_cheese_three():
    assert cheese_three() == "cheese_three passed"
