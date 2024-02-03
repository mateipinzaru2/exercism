"""Functions for compiling dishes and ingredients for a catering company."""

from typing import List, Tuple, Set, Union

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
    # example_dishes,
    # EXAMPLE_INTERSECTION,
)


def clean_ingredients(
    dish_name: str, dish_ingredients: List[str]
) -> Tuple[str, Set[str]]:
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    if not isinstance(dish_name, str):
        raise TypeError("dish_name must be a string")

    if not isinstance(dish_ingredients, (list, set)) or not all(
        isinstance(ingredient, str) for ingredient in dish_ingredients
    ):
        raise TypeError("dish_ingredients must be a list or set of strings")

    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: List[str]) -> str:
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """

    drink_cleaned, drink_ingredients_cleaned = clean_ingredients(
        drink_name, drink_ingredients
    )

    drink_type = (
        "Cocktail" if set(ALCOHOLS) & set(drink_ingredients_cleaned) else "Mocktail"
    )
    return f"{drink_cleaned} {drink_type}"


def categorize_dish(
    dish_name: str, dish_ingredients: List[str]
) -> Union[str, Exception]:
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    dish_cleaned, dish_ingredients_cleaned = clean_ingredients(
        dish_name, dish_ingredients
    )

    categories = {
        "VEGAN": VEGAN,
        "VEGETARIAN": VEGETARIAN,
        "PALEO": PALEO,
        "KETO": KETO,
        "OMNIVORE": OMNIVORE,
    }

    for category, ingredients in categories.items():
        if dish_ingredients_cleaned.issubset(ingredients):
            return f"{dish_cleaned}: {category}"
    return Exception("Dish doesn't fit in any category")


def tag_special_ingredients(dish: Tuple[str, List[str]]) -> Tuple[str, Set[str]]:
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    dish_name, dish_ingredients = dish
    dish_name, dish_ingredients = clean_ingredients(dish_name, dish_ingredients)

    return (dish_name, dish_ingredients & SPECIAL_INGREDIENTS)


def compile_ingredients(dish_list: List[Set[str]]) -> Set[str]:
    """Create a master list of ingredients.

    :param dish_list: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dish_list`.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    return set.union(*dish_list)


def separate_appetizers(dishes: List[str], appetizers: List[str]) -> List[str]:
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: List[Set[str]], intersection: Set[str]) -> Set[str]:
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    if not isinstance(dishes, list) or not all(
        isinstance(dish, set)
        and all(isinstance(ingredient, str) for ingredient in dish)
        for dish in dishes
    ):
        raise TypeError("dishes must be a list of sets of strings")

    if not isinstance(intersection, set) or not all(
        isinstance(ingredient, str) for ingredient in intersection
    ):
        raise TypeError("intersection must be a set of strings")

    singletons = (dish - intersection for dish in dishes)
    return set.union(*singletons)
