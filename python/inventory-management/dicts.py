"""Functions to keep track and alter inventory."""


def valid_items(items):
    """Validate items is a list of strings.

    :param items: list - list to validate.
    :return: bool - True if items is valid, False otherwise.
    """

    if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
        raise TypeError("items must be a list of strings")

    return items


def valid_inventory(inventory):
    """Validate inventory is a dictionary with string keys and integer values.

    :param inventory: dict - dictionary to validate.
    :return: bool - True if inventory is valid, False otherwise.
    """

    if not isinstance(inventory, dict) or not all(
        isinstance(key, str) and isinstance(value, int)
        for key, value in inventory.items()
    ):
        raise TypeError("inventory must be a dict with string keys and integer values")

    return inventory


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    valid_items(items)

    output = {}
    for item in items:
        output[item] = items.count(item)
    return output


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    valid_items(items)
    valid_inventory(inventory)

    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    valid_items(items)
    valid_inventory(inventory)

    for item in items:
        if inventory.get(item, 0) > 0:
            inventory[item] = inventory.get(item, 0) - 1

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    valid_inventory(inventory)
    if not isinstance(item, str):
        raise TypeError("item must be a string")

    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    valid_inventory(inventory)

    output = []
    for key, value in inventory.items():
        if value <= 0:
            continue
        output.append((key, value))
    return output
