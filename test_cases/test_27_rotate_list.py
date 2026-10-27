import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_left():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_empty_list():
    assert rotate_list([], 3) == []


def test_rotation_larger_than_length():
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]


def test_zero_rotation():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]
