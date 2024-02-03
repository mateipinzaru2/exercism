""" https://exercism.org/tracks/python/exercises/resistor-color """

from typing import Union

COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def color_code(color: str) -> Union[int, str]:
    """
    Returns the color code of a given color string

    Args:
        color: string indicating a color

    Returns:
        int: corresponding color code
    """
    if color.lower() not in COLOR_CODES:
        raise ValueError("color must be a string, indicating a known color band")

    return COLOR_CODES.get(color, "No color code for given color")


def colors():
    """
    Gets the color bands as list

    Returns:
        list: band colors
    """

    return list(COLOR_CODES.keys())
