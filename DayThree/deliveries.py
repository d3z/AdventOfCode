direction_deltas = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, 1),
    "v": (0, -1)
}


def take_turn(current_position, delivery_map, direction):
    current_position = tuple([sum(x) for x in zip(current_position, direction_deltas[direction])])
    count_for_position = delivery_map.get(current_position, 0)
    delivery_map[current_position] = count_for_position + 1
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
    delivery_map = {(0, 0): 1}
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
    split_directions = ["", ""]
    for i in range(len(directions)):
        split_directions[i % 2] += directions[i]
    santa_directions, robo_directions = split_directions
    santa_position = (0, 0)
    robo_position = (0, 0)
    delivery_map = {(0, 0): 2}
    for d in range(len(santa_directions)):
        santa_position, delivery_map = take_turn(santa_position, delivery_map, santa_directions[d])
        robo_position, delivery_map = take_turn(robo_position, delivery_map, robo_directions[d])
    return len(delivery_map)

if __name__ == "__main__":
    import doctest

    doctest.testmod("deliveries")
