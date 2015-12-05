import re


def passes_repeated_double_rule(word):
    return re.search("([a-z]{2}).*?\\1", word) is not None


def passes_split_double_rule(word):
    return re.search("(.).{1}\\1", word) is not None


def is_nice_word(word):
    """
    >>> is_nice_word("qjhvhtzxzqqjkmpb")
    True
    >>> is_nice_word("xxyxx")
    True
    >>> is_nice_word("uurcxstgmygtbstg")
    False
    >>> is_nice_word("ieodomkazucvgmuy")
    False
    """
    return passes_repeated_double_rule(word) and \
           passes_split_double_rule(word)



