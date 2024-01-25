"""
raindrops
"""


from typing import Union


DROPS = ("i", 3), ("a", 5), ("o", 7)


def convert(number: Union[int, float]) -> str:
    """
    Convert a number into a string that contains raindrop sounds corresponding to potential factors.
    A factor of 3: Pling, 5: Plang, and 7: Plong.
    If the number does not contain 3, 5, or 7 as a factor, the result should be the number itself.
    """
    if not isinstance(number, (int, float)):
        raise TypeError("number must be int or float")

    return "".join(f"Pl{i}ng" for i, v in DROPS if not number % v) or str(number)
