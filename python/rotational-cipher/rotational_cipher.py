""" 
Program to implement a rotational cipher, 
also known as the Caesar cipher for the English alphabet. 
"""

LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rotate(text: str, key: int) -> str:
    """
    Function to implement the rotational cipher.

    Args:
        text: The text to be encrypted.
        key: The number of places to shift the text.

    Returns:
        The encrypted text.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(key, int) or not 0 <= key <= 26:
        raise ValueError("key must be an int between 0 and 26, inclusively.")

    lower_rotated = LOWER_ALPHABET[key:] + LOWER_ALPHABET[:key]
    upper_rotated = UPPER_ALPHABET[key:] + UPPER_ALPHABET[:key]

    trans = str.maketrans(
        LOWER_ALPHABET + UPPER_ALPHABET, lower_rotated + upper_rotated
    )

    return text.translate(trans)
