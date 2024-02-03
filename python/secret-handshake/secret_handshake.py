""" https://exercism.org/tracks/python/exercises/secret-handshake """

import re

ACTIONS = [
    "wink",
    "double blink",
    "close your eyes",
    "jump",
    "reverse",
]


def strip_string(s):
    """
    Strips string of all characters except 0 and 1

    Args:
        s: a string

    Returns:
        output: s string with all non 0 or 1 characters removed
    """

    return re.sub("[^01]", "", s)


def commands(binary_str: str) -> list[str]:
    """
    Converts a binary string to a list of actions

    Args:
        binary_str: a binary number between 1 and 31, as string

    Returns:
        output: list of strings, representing actions
    """

    stripped = strip_string(binary_str)
    local_actions = ACTIONS[::-1]
    output = []

    if not 0 <= int(stripped, 2) <= 31:
        raise ValueError(
            "binary_str must be a valid binary number between 0 and 31, passed as string"
        )

    for char in stripped[::-1]:
        action = local_actions.pop()
        if char == "1":
            if action == "reverse":
                output = output[::-1]
                continue
            output.append(action)

    return output
