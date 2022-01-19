def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"
def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

a = 4
b = 5
def test_equal1():
    assert a == b, 'Значения разные'
def test_equal2():
    assert a != b, 'Значения разные'

