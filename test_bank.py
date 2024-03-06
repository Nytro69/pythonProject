from bank import value

def test_100():
    assert value("hello") == 100
    assert value("  HEllO  ") == 100

def test_20():
    assert value(" hi ") == 20
    assert value("h") == 20
    assert value("haste") == 20
    assert value("hmm") == 20

def test_0():
    assert value("") == 0
    assert value("   ") == 0
    assert value("kland") == 0
    assert value("... ---- klödjk hello") == 0
    assert value(".hello") == 0