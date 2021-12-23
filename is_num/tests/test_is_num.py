from datetime import datetime

from is_num import is_num


def test_is_num():
    assert is_num(1)


def test_is_not_num():
    assert not is_num("hi")
    assert not is_num({"hi": "apple"})
    assert not is_num(datetime.now())
    assert not is_num(lambda foo: foo)
