"""This module contains the function to classify a number as perfect, abundant, or deficient."""


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if not isinstance(number, int) or not number > 0:
        raise ValueError("Classification is only possible for positive integers.")

    factors = [i for i in range(1, number) if number % i == 0]

    sum_of_factors = sum(factors)

    if sum_of_factors == number:
        return "perfect"

    if sum_of_factors < number:
        return "deficient"

    return "abundant"
