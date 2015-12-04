import hashlib


def find_advent_coin_for(key, size_of_prefix):
    """
    >>> find_advent_coin_for("abcdef", 5)
    609043
    >>> find_advent_coin_for("pqrstuv", 5)
    1048970
    """
    count = 1
    while True:
        candidate = (key + str(count)).encode()
        candidate_hash = hashlib.md5(candidate).hexdigest()
        if candidate_hash[:size_of_prefix] == "0" * size_of_prefix:
            return count
        count += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
