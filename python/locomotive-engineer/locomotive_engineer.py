"""Functions which helps the locomotive engineer to keep track of the train."""


def valid_wagons(wagons):
    """Check if wagons are valid.

    :param wagons: list - the list of wagons.
    :return: wagons.
    """
    for wagon in wagons:
        if not isinstance(wagon, int):
            raise TypeError("Wagons must be a list of integers.")

    return wagons


def valid_route(route):
    """Check if route is valid.

    :param route: dict - the dict of routing information.
    :return: route.
    """
    if (
        not isinstance(route, dict)
        or not len(route.keys()) == 2
        or not set(route.keys()) == {"from", "to"}
    ):
        raise TypeError("Route must be a dict with 2 keys: 'to' and 'from'.")

    if not all(isinstance(value, str) for value in route.values()):
        raise TypeError("Route values must be strings.")

    return route


def valid_wagon_depot(wagons_rows):
    """Check if wagon depot is valid.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: wagons_rows.
    """
    if not isinstance(wagons_rows, list):
        raise TypeError("Wagons rows must be a list.")
    for row in wagons_rows:
        if not isinstance(row, list):
            raise TypeError("Each row must be a list.")
        for wagon in row:
            if not isinstance(wagon, tuple):
                raise TypeError("Each wagon must be a tuple.")
            if not len(wagon) == 2:
                raise TypeError("Each wagon must be a tuple of 2 elements.")
            if not isinstance(wagon[0], int):
                raise TypeError("Each wagon id must be an integer.")
            if not isinstance(wagon[1], str):
                raise TypeError("Each wagon color must be a string.")

    return wagons_rows


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """

    valid_wagons(args)
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    valid_wagons(each_wagons_id)
    valid_wagons(missing_wagons)
    first, second, locomotive, *wagons = each_wagons_id
    return [locomotive, *missing_wagons, *wagons, first, second]


def add_missing_stops(route, **kargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    valid_route(route)
    stops = list(kargs.values())
    return {**route, "stops": stops}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """

    if not isinstance(more_route_information, dict):
        raise TypeError("More route information must be a dict.")
    valid_route(route)
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    valid_wagon_depot(wagons_rows)
    return [list(wagon) for wagon in zip(*wagons_rows)]
