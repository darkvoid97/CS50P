from numb3rs import validate

def test_validate():
    assert validate("192.168.0.1") == True
    assert validate("127.0.0.1") == True
    assert validate("275.165.89.90") == False
    assert validate("0.0.0.0") == True
    assert validate("255.001.002.3") == False
    assert validate("192.168.00.01") == False
