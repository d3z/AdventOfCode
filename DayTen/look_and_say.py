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
    current = digits[:1]
    count = 1
    output = ""
    for digit in digits[1:]:
        if digit == current:
            count += 1
        else:
            output += str(count) + current
            current = digit
            count = 1
    output += str(count) + current
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
