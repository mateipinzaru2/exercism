""" https://exercism.org/tracks/python/exercises/resistor-color-trio """

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

MAGNITUDES = {
    "quetta": 30,
    "ronna": 27,
    "yotta": 24,
    "zetta": 21,
    "exa": 18,
    "peta": 15,
    "tera": 12,
    "giga": 9,
    "mega": 6,
    "kilo": 3,
}


def label(colors: list[str]) -> str:
    """
    Returns resistor label given a list of known resistor band colors

    Args:
        colors: list of strings indicating known resistor band colors

    Returns:
        label: string representing resistor value
        For example, the input ["orange", "orange", "black"] returns "33 ohms"
    """

    if (
        not isinstance(colors, list)
        or not all(isinstance(color, str) for color in colors)
        or not len(colors) >= 3
        or not all(color.lower() in COLOR_CODES for color in colors)
    ):
        raise ValueError(
            "colors must be a list of 3 strings, each representing a known resistor color band"
        )

    first, second, third, *_ = [COLOR_CODES[color.lower()] for color in colors]
    ohms = (first * 10 + second) * (10**third)

    for magnitude_name, magnitude_value in sorted(
        MAGNITUDES.items(), key=lambda item: item[1], reverse=True
    ):
        if ohms >= 10**magnitude_value:
            ohms /= 10**magnitude_value
            magnitude = magnitude_name + "ohms"
            break
    else:
        magnitude = "ohms"

    return f"{int(ohms)} {magnitude}"
