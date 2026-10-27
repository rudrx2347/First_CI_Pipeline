import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_normal_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty_list():
    assert bubble_sort([]) == []


def test_single_element():
    assert bubble_sort([7]) == [7]


def test_negative_numbers():
    assert bubble_sort([-3, 5, -1, 0]) == [-3, -1, 0, 5]


def test_original_list_unchanged():
    numbers = [3, 1, 2]
    bubble_sort(numbers)
    assert numbers == [3, 1, 2]
