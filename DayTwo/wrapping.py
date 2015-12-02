


def wrapping(dimensions):
    """
    Calculates the wrapping paper needed for a
    package of the given dimensions
    >>> wrapping([2, 3, 4])
    58
    >>> wrapping([1, 1, 10])
    43
    """
    [size1, size2, size3] = dimensions
    return (3 * (size1 * size2)) + (2 * (size2 * size3)) + (2 * (size1 * size3))


def ribbon(dimensions):
    """
    Calculates the total amount of ribbon required
    >>> ribbon([2, 3, 4])
    34
    >>> ribbon([1, 1, 10])
    14
    """
    [size1, size2, size3] = dimensions
    return (size1 * size2 * size3) + (2 * size1) + (2 * size2)


def total_for(input_file):
    sizes = [line.strip().split("x") for line in open(input_file).readlines()]

    total_wrapping = 0
    total_ribbon = 0

    for size in sizes:
        size = list(map(lambda s: int(s), size))
        size.sort()
        total_wrapping += wrapping(size)
        total_ribbon += ribbon(size)
    return {"wrapping": total_wrapping, "ribbon": total_ribbon}

if __name__ == "__main__":
    import doctest
    doctest.testmod()