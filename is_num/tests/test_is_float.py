from datetime import datetime

from is_num import is_float


def test_is_float():
    assert is_float(1.1)

    assert not is_float(1)
    assert not is_float(1.0)
    assert not is_float("hi apple")
    assert not is_float({"hi": "apple"})
    assert not is_float(datetime.now())
    assert not is_float(lambda foo: foo)
