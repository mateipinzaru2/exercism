"""
Exercism - reverse string
"""


def reverse(text: str) -> str:
    """
    Reverses the string passed into the function
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return text[::-1]
