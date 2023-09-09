import pytest

@pytest.fixture
def int_num():
    return 123

@pytest.fixture
def str_num():
    return "123"

@pytest.fixture
def float_num():
    return 123.5