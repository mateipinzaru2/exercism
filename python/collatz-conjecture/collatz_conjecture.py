""" 
This module contains the function steps that calculates
the number of steps required to reach 1 in the Collatz Conjecture. 
"""


def steps(number: int) -> int:
    """
    Calculate the number of steps required to reach 1 in the Collatz Conjecture.

    :param number: int - the number to start with.
    :return: int - the number of steps required to reach 1.
    """

    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    output = 0
    while number != 1:
        number = number // 2 if number % 2 == 0 else number * 3 + 1
        output += 1
    return output
