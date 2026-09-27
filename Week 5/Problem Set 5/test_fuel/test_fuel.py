import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    assert convert("3/5") == 60

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(60) == "60%"

def test_valueError():
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/-4")

def test_zeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
