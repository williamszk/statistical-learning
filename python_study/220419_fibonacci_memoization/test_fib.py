from fib import Fib


def test_fib_of_index_1():
    assert Fib.calculate(0) == 1


def test_fib_of_index_5():
    assert Fib.calculate(5) == 8


def test_fib_of_index_9():
    assert Fib.calculate(9) == 55


def test_fib_of_index_10():
    assert Fib.calculate(10) == 89


def test_fib_of_index_6():
    assert Fib.calculate(6) == 13
