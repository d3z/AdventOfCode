from json import loads


def add_add_numbers_in(thing):
    total = 0
    for i in thing:
        if type(i) == int:
            total += i
        elif type(i) == list:
            total += add_add_numbers_in(i)
        elif type(i) == dict and "red" not in i.values():
                total += add_add_numbers_in(i.values())
    return total


def add_all_numbers(json_string):
    '''
    >>> add_all_numbers("[1,2,3]")
    6
    >>> add_all_numbers('[{"a":2,"b":4}]')
    6
    >>> add_all_numbers('[[1], {"a":"red", "b":2}]')
    1
    '''
    data = loads(json_string)
    return add_add_numbers_in(data)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
