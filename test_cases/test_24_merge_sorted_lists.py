import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_merge_normal_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_empty_lists():
    assert merge_sorted_lists([], []) == []


def test_first_list_empty():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_second_list_empty():
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_duplicates_and_negative_numbers():
    assert merge_sorted_lists([-3, 1, 2], [-2, 1, 4]) == [-3, -2, 1, 1, 2, 4]
