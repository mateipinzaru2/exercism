"""
Returns the earned points in a single toss of a Darts game.
"""

from typing import Union
from math import sqrt


def score(x: Union[int, float], y: Union[int, float]) -> int:
    """
    Returns the earned points in a single toss of a Darts game.

    Args:
    x (int, float): x-coordinate of the dart.
    y (int, float): y-coordinate of the dart.

    Returns:
    float: The earned points in a single toss of a Darts game.
    """

    distance = sqrt(x**2 + y**2)

    if distance > 10:
        return 0
    if distance > 5:
        return 1
    if distance > 1:
        return 5
    return 10
