import pytest

from jaime import sum, sub, cola


def test_sum():
    assert sum(1, 2) == 3
    assert sum(1, 1) == 2
    assert sum(105, 321) == 426


def test_sub():
    assert sub(2, 1) == 1
    assert sub(5, 5) == 0


def test_firstlast():
    c = cola()

    c.ingresa(5)
    c.ingresa(17)
    c.ingresa("hello")

    assert c.primero() == 5
    assert c.ultimo() == "hello"


def test_len():
    c = cola()

    assert c.length() == 0

    c.ingresa(1)

    assert c.length() == 1

    for i in range(10):
        c.ingresa(i)

    assert c.length() == 11

@pytest.mark.parametrize("a, b, c", [(10,20, 30), (20,40,60), (11,22,33)])
def test_add(a, b, c):
    res = sum(a, b)
    assert res == c
