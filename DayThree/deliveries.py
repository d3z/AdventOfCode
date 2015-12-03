direction_deltas = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, 1),
    "v": (0, -1)
}


def build_map_for(directions):
    delivery_map = {(0, 0): 1}
    current_position = (0, 0)
    for direction in directions:
        current_position = tuple([sum(x) for x in zip(current_position, direction_deltas[direction])])
        count_for_position = delivery_map.get(current_position, 0)
        delivery_map[current_position] = count_for_position + 1
    return delivery_map


def got_at_least_one_present(directions):
    """
    >>> got_at_least_one_present(">")
    2
    >>> got_at_least_one_present("^>v<")
    4
    >>> got_at_least_one_present("^v^v^v^v^v")
    2
    """
    return len(build_map_for(directions))


if __name__ == "__main__":
    import doctest

    doctest.testmod("deliveries")
