""" Program that takes in a number between 0 and 3999 as argument and returns a Roman numeral. """

ROMANS = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def roman(number: int) -> str:
    """
    Convert a number to Roman numerals.

    Args:
        number: The number to convert. Must be between 0 and 3999.

    Returns:
        The Roman numeral representation of the number.

    Raises:
        ValueError: If the number is not between 0 and 3999.
    """

    if not isinstance(number, int) or not 0 <= number <= 3999:
        raise ValueError("Number must be int between 0 and 3999.")

    result = ""
    for key, value in sorted(ROMANS.items(), key=lambda item: item[1], reverse=True):
        count, number = divmod(number, value)
        result += key * count

    return result
