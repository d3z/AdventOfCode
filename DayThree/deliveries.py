from collections import defaultdict

direction_deltas = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, 1),
    "v": (0, -1)
}


def take_turn(current_position, delivery_map, direction):
    current_position = tuple([sum(x) for x in zip(current_position, direction_deltas[direction])])
    delivery_map[current_position] += 1
    return current_position, delivery_map


def got_at_least_one_present(directions):
    """
    >>> got_at_least_one_present(">")
    2
    >>> got_at_least_one_present("^>v<")
    4
    >>> got_at_least_one_present("^v^v^v^v^v")
    2
    """
    current_position = (0, 0)
    delivery_map = defaultdict(int, {(0, 0): 0})
    for direction in directions:
        current_position, delivery_map = take_turn(current_position, delivery_map, direction)
    return len(delivery_map)


def with_robo_santa(directions):
    """
    >>> with_robo_santa("^v")
    3
    >>> with_robo_santa("^>v<")
    3
    >>> with_robo_santa("^v^v^v^v^v")
    11
    """
    positions = [(0, 0), (0, 0)]
    delivery_map = defaultdict(int, {(0, 0): 2})
    for x in range(len(directions)):
        positions[x % 2], delivery_map = take_turn(positions[x % 2], delivery_map, directions[x])
    return len(delivery_map)


if __name__ == "__main__":
    import doctest

    doctest.testmod("deliveries")
