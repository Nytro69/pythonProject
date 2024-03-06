from fuel import percent

def test_e_f():
    assert percent("1/1000") == "E"
    assert percent("1/1") == "F"

def test_zero():
    assert percent("1/0") == False
    assert percent("0/1") == "E"

def test_random_problems():
    assert percent("1/2") == 50
    assert percent("9/10") == 90