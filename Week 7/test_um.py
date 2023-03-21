from um import count

def test_um_inside():
    assert count("um mum numb thumb um") == 2

def test_no_um():
    assert count("Not in this one yo.") == 0

def test_cap_punc_um():
    assert count("Ummm... So like Mum, um, this is UM, Yummy?") == 2
