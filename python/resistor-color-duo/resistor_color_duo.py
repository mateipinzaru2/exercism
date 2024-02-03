""" https://exercism.org/tracks/python/exercises/resistor-color-duo """

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


def value(colors: list[str]) -> int:
    """
    Returns the color code of a given color, or two-color combination
    ex: "brown" would return 1; "brown-green" would return 15

    Args:
        colors: list of color strings

    Returns:
        int: corresponding color code
    """

    if not isinstance(colors, list) or not all(
        isinstance(color, str) for color in colors
    ):
        raise TypeError("colors must be list of color strings")

    output = [
        str(COLOR_CODES[color.lower()])
        for color in colors
        if color.lower() in COLOR_CODES
    ][:2]

    return int("".join(output))
