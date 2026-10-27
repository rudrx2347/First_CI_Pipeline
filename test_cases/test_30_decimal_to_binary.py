import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_normal_number():
    assert decimal_to_binary(10) == "1010"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_power_of_two():
    assert decimal_to_binary(8) == "1000"


def test_single_digit():
    assert decimal_to_binary(1) == "1"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)
