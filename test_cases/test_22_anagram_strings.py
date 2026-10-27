import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_basic_anagram():
    assert is_anagram("listen", "silent") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_uppercase_ignored():
    assert is_anagram("Listen", "Silent") is True


def test_spaces_ignored():
    assert is_anagram("conversation", "voices rant on") is True


def test_different_lengths():
    assert is_anagram("cat", "cats") is False
