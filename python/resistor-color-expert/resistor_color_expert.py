""" https://exercism.org/tracks/python/exercises/resistor-color-expert """

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

TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors: list[str]) -> str:
    """
    Translates resistor color bands to human-readable labels

    Args:
        colors: list of color bands

    Returns:
        label: reistor label
    """

    if (
        not isinstance(colors, list)
        or not all(isinstance(color, str) for color in colors)
        or len(colors) not in (1, 4, 5)
        or not all(color.lower() in COLOR_CODES for color in colors)
    ):
        raise ValueError(
            "colors must be a list of strings, indicating known color bands"
        )

    if len(colors) > 3:
        *values, multiplier, tolerance = colors
    else:
        values, multiplier, tolerance = colors, "black", None

    ohms = 0
    for value in values:
        ohms = ohms * 10 + COLOR_CODES[value]
    ohms *= 10 ** COLOR_CODES[multiplier]

    for magnitude_name, magnitude_value in sorted(
        MAGNITUDES.items(), key=lambda item: item[1], reverse=True
    ):
        if ohms >= 10**magnitude_value:
            ohms /= 10**magnitude_value
            magnitude = magnitude_name + "ohms"
            break
    else:
        magnitude = "ohms"

    return (
        f"{ohms:n} {magnitude} ±{TOLERANCES[tolerance]}%"
        if tolerance in TOLERANCES
        else f"{ohms:n} {magnitude}"
    )
