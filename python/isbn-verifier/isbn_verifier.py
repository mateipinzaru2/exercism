""" Program has a function that checks if a given ISBN is valid or not. """


def is_valid(isbn: str) -> bool:
    """
    Function checks if a given ISBN is valid or not.

    Args:
        isbn: A string of characters.

    Returns:
        True if the ISBN is valid, False otherwise.
    """

    stripped = isbn.replace("-", "")

    if (
        len(stripped) != 10
        or not stripped[:-1].isdigit()
        or stripped[-1] not in "0123456789X"
    ):
        return False

    stripped = [int(num) if num != "X" else 10 for num in stripped]

    return sum(stripped[i] * (10 - i) for i in range(10)) % 11 == 0
