"""Functions to help Azara and Rui locate pirate treasure."""


def valid_azara_record(record):
    """
    Checks if a tuple forms a validate coordinate
    """

    if (
        not isinstance(record, tuple)
        or not all(isinstance(elem, str) for elem in record)
        or not len(record) == 2
        or not len(record[1]) == 2
    ):
        raise TypeError(
            """
            azara_record must be a tuple of exactly 2 strings, 
            where the first element is a location 
            and the second is a 2 character location (ex: 2D)
            """
        )

    return record


def valid_rui_record(record):
    """
    Checks if a tuple forms a validate coordinate
    """

    if (
        not isinstance(record, tuple)
        or not len(record) == 3
        or not record[1][0].isdigit()
        or not record[1][1].isalpha()
        or not record[1][1].isupper()
    ):
        raise TypeError(
            """
            rui_record must be a tuple of exactly 3 elements, 
            where the first element is a string indicating a location, 
            the second is a 2 character tuple, ex: ("1", "C"),
            and the third is a quadrant, ex: Blue
            """
        )

    return record


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    if valid_azara_record(record):
        return record[1]
    return None


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    if not isinstance(coordinate, str) and not len(coordinate) == 2:
        raise TypeError("coordinate must be a string of 2 characters in length")

    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    if not valid_azara_record(azara_record) or not valid_rui_record(rui_record):
        raise TypeError(
            """
            azara_record must be a tuple: (treasure, coordinate)
            rui_record must be a tuple: (location, tuple(coordinate_1, coordinate_2), quadrant)
            """
        )

    if rui_record[1] == convert_coordinate(get_coordinate(azara_record)):
        return True
    return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if not valid_azara_record(azara_record) or not valid_rui_record(rui_record):
        raise TypeError(
            """
            azara_record must be a tuple: (treasure, coordinate)
            rui_record must be a tuple: (location, tuple(coordinate_1, coordinate_2), quadrant)
            """
        )

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    if not isinstance(combined_record_group, tuple) or not all(
        isinstance(item, tuple) for item in combined_record_group
    ):
        raise TypeError("combined_record_group must be a tuple")

    cleaned_records = []
    for item in combined_record_group:
        mutate = list(item)
        del mutate[1]
        cleaned_records.append(str(tuple(mutate)))

    return "\n".join(cleaned_records) + "\n"
