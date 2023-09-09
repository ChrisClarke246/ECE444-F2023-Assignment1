
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

def test_formatter_string(str_num):
    with pytest.raises(AssertionError):
        Utils.formatter(str_num)

def test_formatter_float(float_num):
    with pytest.raises(AssertionError):
        Utils.formatter(float_num)
    
def test_formatter_int(int_num):
    res_binary, res_base_8 = Utils.formatter(int_num)
    assert res_binary == 0b111011
    assert res_base_8 == 0o173