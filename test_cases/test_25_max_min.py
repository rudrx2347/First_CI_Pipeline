import importlib
import pytest

module = importlib.import_module("25_max_min")
find_max_min = module.find_max_min


def test_normal_list():
    assert find_max_min([3, 1, 9, 5]) == (9, 1)


def test_single_element():
    assert find_max_min([7]) == (7, 7)


def test_negative_numbers():
    assert find_max_min([-5, -2, -9]) == (-2, -9)


def test_mixed_numbers():
    assert find_max_min([-10, 0, 8, 3]) == (8, -10)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])
