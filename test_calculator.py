
import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(5, 3) == 8

def test_subtract():
    assert calc.subtract(10, 4) == 6

def test_multiply():
    assert calc.multiply(3, 4) == 12

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_add_negative_numbers():
    assert calc.add(-5, -3) == -8

def test_multiply_by_zero():
    assert calc.multiply(5, 0) == 0
