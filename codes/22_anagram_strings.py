"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()
    return sorted(first) == sorted(second)
