"""
checks if input is Armstrong number
"""


def is_armstrong_number(number: int) -> bool:
    """
    Check if a number is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits
    each raised to the power of the number of digits.

    :param number: int - The number to check.
    :return: bool - True if the number is an Armstrong number, False otherwise.
    :raises ValueError: If the input is not a positive integer.
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")
    digits = [int(digit) for digit in str(number)]
    return sum(digit ** len(digits) for digit in digits) == number
