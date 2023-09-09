
import pytest
from utils import Utils

def test_reversed_strings(str_num):
    with pytest.raises(AssertionError):
        Utils.reversed(str_num)

def test_reversd_floats(float_num):
    with pytest.raises(AssertionError):
        Utils.reversed(float_num)

def test_reversd_int(int_num):
    res = Utils.reversed(int_num)
    assert res == 321