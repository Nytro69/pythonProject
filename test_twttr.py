from twttr import str_conversion

def test_upper():
    assert str_conversion("HELLO EVERYONE") == "HLL VRYN"
    assert str_conversion("KHL  ") == "KHL  "

def test_lower():
    assert str_conversion("hello to not everyone") == "hll t nt vryn"
    assert str_conversion("jk...") == "jk..."

def test_punctuation():
    assert str_conversion("..  .- --  -... . ... -") == "..  .- --  -... . ... -"
    assert str_conversion("-- o --") == "--  --"

def test_nothing():
    assert str_conversion("") == ""