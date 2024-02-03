""" Program contains function to check if string makes up an English pangram. """


def is_pangram(sentence):
    """
    Function checks if a given string is a pangram.

    Args:
    sentence: string to be checked for pangram.

    Returns:
    True: if sentence is a pangram.
    """

    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")

    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    stripped = sentence.lower().replace(" ", "")
    return set(stripped) >= alphabet
