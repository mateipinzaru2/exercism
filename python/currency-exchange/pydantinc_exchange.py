from typing import Union
from pydantic import validate_call


@validate_call
def exchange_money(
    budget: Union[float, int], exchange_rate: Union[float, int]
) -> float:
    """
    Exchange money from one currency to another.

    :param budget: float or int - amount of money you are planning to exchange.
    :param exchange_rate: float or int - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    :raises: ValueError if budget or exchange_rate are not positive.
    """

    if budget <= 0 or exchange_rate <= 0:
        raise ValueError("Budget and exchange rate must be positive.")

    return budget / exchange_rate


@validate_call
def get_change(budget: Union[float, int], exchanging_value: Union[float, int]) -> float:
    """
    Calculate the amount of money you have left after exchanging.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    if budget <= 0 or budget < exchanging_value <= 0:
        raise ValueError("Budget must be positive and greater than exchanging value.")

    return budget - exchanging_value


@validate_call
def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """
    Calculate the value of the bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    if denomination <= 0 or number_of_bills <= 0:
        raise ValueError("Denomination and number of bills must be positive.")

    return denomination * number_of_bills


@validate_call
def get_number_of_bills(amount: Union[int, float], denomination: int) -> int:
    """
    Calculate the number of bills that can be obtained from the amount.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    if amount <= 0 or denomination <= 0:
        raise ValueError("Amount and denomination must be positive.")

    return amount // denomination


@validate_call
def get_leftover_of_bills(amount: Union[float, int], denomination: int) -> float:
    """
    Calculate the amount that is "leftover", given the current denomination.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    if amount <= 0 or denomination <= 0:
        raise ValueError("Amount and denomination must be positive.")

    return amount % denomination


@validate_call
def exchangeable_value(
    budget: Union[float, int],
    exchange_rate: Union[float, int],
    spread: int,
    denomination: int,
) -> int:
    """
    Calculate the maximum value you can get.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    if budget <= 0 or exchange_rate <= 0 or denomination <= 0:
        raise ValueError("Budget, exchange rate, and denomination must be positive.")

    exchange_rate = exchange_rate * (1 + spread / 100)
    exchanged = exchange_money(budget, exchange_rate)
    tax = get_leftover_of_bills(exchanged, denomination)
    return int(exchanged - tax)
