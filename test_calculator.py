import pytest

from calculator import Calculator


def test_calculator_cases():
    """Run table-driven test cases for the basic calculator operations."""
    calculator = Calculator()

    test_cases = [
        (calculator.add, 5, 3, 8),
        (calculator.add, 10, 20, 30),
        (calculator.subtract, 10, 4, 6),
        (calculator.subtract, 5, 8, -3),
        (calculator.multiply, 4, 5, 20),
        (calculator.multiply, 3, 0, 0),
        (calculator.divide, 10, 2, 5),
        (calculator.divide, 9, 3, 3),
    ]

    for operation, a, b, expected in test_cases:
        assert operation(a, b) == expected


def test_divide_by_zero():
    calculator = Calculator()

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
