from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("CS") == True

def test_first_char():
    assert is_valid("1KL") == False
    assert is_valid("KL1") == True

def test_middle():
    assert is_valid("NUM9K") == False
    assert is_valid("G111I") == False

def test_first_int_zero():
    assert is_valid("KK01") == False
    assert is_valid("KK10") == True