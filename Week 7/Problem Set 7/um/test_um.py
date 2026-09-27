from um import count

def test_validate():
    assert count("um") == 1
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("Um, hey!") == 1
    assert count("uM, hEY!") == 1
    assert count("UM HEY, I AM, UM, YELLING BECAUSE I WANT MY MUM WHILE I'M PLAYING DRUMS!") == 2
