import re


def passes_vowel_rule(word):
    return re.search("(.*?[aeiou].*?){3}", word) is not None


def passes_doubles_rule(word):
    return re.search("([a-z])\\1", word) is not None


def passes_exclusions_rule(word):
    return re.search("ab|cd|pq|xy", word) is None


def is_nice_word(word):
    """
    >>> is_nice_word("ugknbfddgicrmopn")
    True
    >>> is_nice_word("aaa")
    True
    >>> is_nice_word("jchzalrnumimnmhp")
    False
    >>> is_nice_word("haegwjzuvuyypxyu")
    False
    >>> is_nice_word("dvszwmarrgswjxmb")
    False
    """
    return passes_vowel_rule(word) and \
           passes_doubles_rule(word) and \
           passes_exclusions_rule(word)



