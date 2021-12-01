import pytest

def sum_1(number):
    return int(number) + 1



def test_sum_1():
    assert sum_1(41) == 42


def test_sum_1_number_as_string():
    assert sum_1("41") == 42


def test_sum_a_word():
    with pytest.raises(ValueError):
        sum_1("hello there!")











