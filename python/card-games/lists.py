"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

from typing import List


def get_rounds(number: int) -> List[int]:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    if (
        not isinstance(rounds_1, list)
        or not isinstance(rounds_2, list)
        or not all(isinstance(round_num, int) for round_num in rounds_1)
        or not all(isinstance(round_num, int) for round_num in rounds_2)
    ):
        raise TypeError("Rounds must be lists of ints.")

    return rounds_1 + rounds_2


def list_contains_round(rounds: List[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if (
        not isinstance(rounds, list)
        or not all(isinstance(card, int) for card in rounds)
        or not isinstance(number, int)
    ):
        raise TypeError("Rounds must be a list of ints and number must be an int.")

    return number in rounds


def card_average(hand: List[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    if not isinstance(hand, list) or not all(isinstance(card, int) for card in hand):
        raise TypeError("Hand must be a list of ints.")

    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    if not isinstance(hand, list) or not all(isinstance(card, int) for card in hand):
        raise TypeError("Hand must be a list of ints.")

    return (hand[0] + hand[-1]) / 2 == card_average(hand) or hand[
        len(hand) // 2
    ] == card_average(hand)


def average_even_is_average_odd(hand: List[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    if not isinstance(hand, list) or not all(isinstance(card, int) for card in hand):
        raise TypeError("Hand must be a list of ints.")

    return card_average(hand[::2]) == card_average(hand[1::2])


def maybe_double_last(hand: List[int]) -> List[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if not isinstance(hand, list) or not all(isinstance(card, int) for card in hand):
        raise TypeError("Hand must be a list of ints.")

    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
