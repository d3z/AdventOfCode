from itertools import groupby

def parse(digits):
    '''
    >>> parse("1")
    '11'
    >>> parse("11")
    '21'
    >>> parse("21")
    '1211'
    >>> parse("1211")
    '111221'
    >>> parse("111221")
    '312211'
    '''
    return "".join([str(len([0 for _ in g])) + str(k) for k, g in groupby(digits)])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
