from plates import is_valid

def test_length():
    assert is_valid("HELLOWORLD") == False
    assert is_valid("HL") == True
    assert is_valid("CS50") == True
    assert is_valid("Z") == False
    assert is_valid("SIXLTR") == True

def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("AA222A") == False
    assert is_valid("AAA022") == False

def test_beginning():
    assert is_valid("HVCS50") == True
    assert is_valid("50HVCS") == False
    assert is_valid("5HVCS0") == False
    assert is_valid("5CS0") == False
    assert is_valid("50") == False
    assert is_valid("CS") == True
    assert is_valid("5") == False
    assert is_valid("C5") == False

def test_punctuation():
    assert is_valid(".CS50.") == False
    assert is_valid("H3770!") == False
    assert is_valid("HVDCS?") == False
