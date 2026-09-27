from twttr import shorten

def test_shorten():
    assert shorten("Hello World!") == "Hll Wrld!"
    assert shorten("hello world") == "hll wrld"
    assert shorten("CS50") == "CS50"
    assert shorten("Ciao") == "C"
    assert shorten("Ahoy!") == "hy!"
