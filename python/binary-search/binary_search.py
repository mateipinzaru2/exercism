""" https://exercism.org/tracks/python/exercises/binary-search """


def find(search_list: list[int], value: int) -> int:
    """
    Function that returns the value's index if found in the search list.

    Args:
        search_list: list of ints
        value: int to search for

    Returns:
        int: value's index in search_list
    """

    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] < value:
            low = mid + 1
        elif search_list[mid] > value:
            high = mid - 1
        else:
            return mid

    raise ValueError("value not in array")
