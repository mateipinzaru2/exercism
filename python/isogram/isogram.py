""" Program contains a function that checks if a word is an isogram. """


def is_isogram(string: str) -> bool:
    """
    Function checks if a word is an isogram.

    Args:
        string: A string of characters.

    Returns:
        True if the string is an isogram, False otherwise.
    """

    if not isinstance(string, str):
        raise TypeError("Argument must be a string")

    lowered = string.lower()
    alpha_chars = [char for char in lowered if char.isalpha()]

    return len(alpha_chars) == len(set(alpha_chars))
