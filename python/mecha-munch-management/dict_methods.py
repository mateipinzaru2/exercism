"""Functions to manage a users shopping cart items."""


from typing import Iterable


def valid_cart(cart: dict) -> dict:
    """
    Checks if dict is valid cart
    """

    if not isinstance(cart, dict) or not all(
        isinstance(key, str) and isinstance(value, int) for key, value in cart.items()
    ):
        raise TypeError("cart must be a dict with string keys and int values.")

    return cart


def valid_iterable(items: Iterable) -> Iterable:
    """
    Checks if input is valid Iterable
    """
    if not isinstance(items, Iterable):
        raise TypeError("items must be an iterable")

    return items


def valid_recipes(recipes: Iterable) -> Iterable:
    """
    Checks if recipes is a valid Iterable of tuple recipes
    """

    if not valid_iterable(recipes) or not all(
        isinstance(update, tuple)
        and len(update) == 2
        and isinstance(update[0], str)
        and isinstance(update[1], dict)
        for update in recipes
    ):
        raise TypeError(
            "recipes must be an Iterable of tuples, where each contains a string and a dict"
        )

    return recipes


def valid_recipe_updates(updates: dict) -> dict:
    """
    Checks if updates is a valid dict of carts
    """
    if not isinstance(updates, dict) or not all(
        isinstance(recipe_name, str) and valid_cart(recipe)
        for recipe_name, recipe in updates.items()
    ):
        raise TypeError("updates must be a dict of dicts, where each key is ")

    return updates


def valid_isle_mappings(isle_mapping: dict) -> dict:
    """
    Checks if valid isle_mapping dict
    """
    if not isinstance(isle_mapping, dict) or not all(
        (
            isinstance(isle, str) and isinstance(needs_refrige, bool)
            for isle, needs_refrige in isle_mappings
        )
        for isle_mappings in isle_mapping.values()
    ):
        raise TypeError(
            "isle_mapping must be a dict with string keys and [str, bool] values"
        )

    return isle_mapping


def valid_store_inventory(store_inventory: dict) -> dict:
    """
    Checks if valid store_inventory dict
    """

    if not isinstance(store_inventory, dict) or not all(
        (
            isinstance(quantity, int)
            and isinstance(isle, str)
            and isinstance(needs_refrige, bool)
            for quantity, isle, needs_refrige in isle_mappings
        )
        for isle_mappings in store_inventory.values()
    ):
        raise TypeError(
            "store_inventory must be a dict with string keys and [int, str, bool] values"
        )

    return store_inventory


def add_item(current_cart: dict, items_to_add: Iterable) -> dict:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    valid_cart(current_cart)

    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1

    return current_cart


def read_notes(notes: Iterable) -> dict:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    valid_iterable(notes)

    return dict.fromkeys(notes, 1)


def update_recipes(ideas: dict, recipe_updates: Iterable) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: Iterable - containing dictionaries with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas = valid_recipe_updates(ideas)
    recipe_updates = valid_recipes(recipe_updates)

    ideas.update({update[0]: update[1] for update in recipe_updates})

    return ideas


def sort_entries(cart: dict) -> dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    cart = valid_cart(cart)
    return dict(sorted(cart.items()))


def send_to_store(cart: dict, isle_mapping: dict) -> dict:
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    if cart.keys() != isle_mapping.keys():
        raise ValueError("cart and isle_mapping must have the same keys")

    isle_mapping = valid_isle_mappings(isle_mapping)
    cart = valid_cart(cart)

    output = {
        cart_key: [cart_value] + isle_mapping[cart_key]
        for cart_key, cart_value in cart.items()
    }

    return dict(reversed(sorted(output.items())))


def update_store_inventory(fulfillment_cart: dict, store_inventory: dict) -> dict:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    fulfillment_cart = valid_store_inventory(fulfillment_cart)
    store_inventory = valid_store_inventory(store_inventory)

    for fulfillment_key in fulfillment_cart.keys():
        if fulfillment_key in store_inventory.keys():
            store_amount, *store_unpacked = store_inventory[fulfillment_key]
            fulfill_amount = fulfillment_cart[fulfillment_key][0]
            dif_amount = (
                store_amount - fulfill_amount
                if (store_amount - fulfill_amount) > 0
                else "Out of Stock"
            )
            store_inventory[fulfillment_key] = [dif_amount] + store_unpacked

    return store_inventory
