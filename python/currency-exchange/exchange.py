def exchange_money(budget, exchange_rate):
    """
    Exchange money from one currency to another.

    :param budget: float or int - amount of money you are planning to exchange.
    :param exchange_rate: float or int - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    :raises: ValueError if budget or exchange_rate are not positive.
    """

    if not isinstance(budget, (int, float)) or not isinstance(
        exchange_rate, (int, float)
    ):
        raise TypeError("Budget and exchange rate must be numbers.")
    if budget <= 0 or exchange_rate <= 0:
        raise ValueError("Budget and exchange rate must be positive.")
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Calculate the amount of money you have left after exchanging.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    if not isinstance(budget, (int, float)) or not isinstance(
        exchanging_value, (int, float)
    ):
        raise TypeError("Budget and exchanging value must be numbers.")
    if budget <= 0 or budget < exchanging_value <= 0:
        raise ValueError("Budget must be positive and greater than exchanging value.")
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the value of the bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    if not isinstance(denomination, int) or not isinstance(number_of_bills, int):
        raise TypeError("Denomination and number of bills must be integers.")
    if denomination <= 0 or number_of_bills <= 0:
        raise ValueError("Denomination and number of bills must be positive.")
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Calculate the number of bills that can be obtained from the amount.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    if not isinstance(amount, (int, float)) or not isinstance(denomination, int):
        raise TypeError("Amount must be a number and denomination must be an integer.")
    if amount <= 0 or denomination <= 0:
        raise ValueError("Amount and denomination must be positive.")
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """
    Calculate the amount that is "leftover", given the current denomination.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    if not isinstance(amount, (int, float)) or not isinstance(denomination, int):
        raise TypeError("Amount must be a number and denomination must be an integer.")
    if amount <= 0 or denomination <= 0:
        raise ValueError("Amount and denomination must be positive.")
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum value you can get.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    if (
        not isinstance(budget, (int, float))
        or not isinstance(exchange_rate, (int, float))
        or not isinstance(spread, int)
        or not isinstance(denomination, int)
    ):
        raise TypeError(
            "Budget and exchange rate must be numbers, spread and denomination must be integers."
        )
    if budget <= 0 or exchange_rate <= 0 or denomination <= 0:
        raise ValueError("Budget, exchange rate, and denomination must be positive.")
    exchange_rate = exchange_rate * (1 + spread / 100)
    exchanged = exchange_money(budget, exchange_rate)
    tax = get_leftover_of_bills(exchanged, denomination)
    return int(exchanged - tax)
