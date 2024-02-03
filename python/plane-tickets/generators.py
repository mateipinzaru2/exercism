"""Functions to automate Conda airlines ticketing system."""

from typing import Generator, List, Dict


SEATS = ["A", "B", "C", "D"]


def generate_seat_letters(number: int) -> Generator[str, None, None]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    if not isinstance(number, int):
        raise ValueError("number must be int")

    current_index = 0
    for _ in range(number):
        yield SEATS[current_index]
        current_index = (current_index + 1) % len(SEATS)


def generate_seats(number: int) -> Generator[str, None, None]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    if not isinstance(number, int):
        raise ValueError("number must be int")

    seat_letter = generate_seat_letters(number)

    for i in range(number):
        row = i // len(SEATS) + 1
        if row >= 13:
            row += 1
        try:
            letter = next(seat_letter)
        except StopIteration:
            return
        yield str(row) + letter


def assign_seats(passengers: List[str]) -> Dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    if not isinstance(passengers, list) or not all(
        isinstance(passenger, str) for passenger in passengers
    ):
        raise ValueError("passengers must be a list of strings")

    output = {}
    seat = generate_seats(len(passengers))
    for passenger in passengers:
        output[passenger] = next(seat, None)
    return output


def generate_codes(
    seat_numbers: List[str], flight_id: str
) -> Generator[str, None, None]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    if not isinstance(seat_numbers, list) or not all(
        isinstance(seat_number, str) for seat_number in seat_numbers
    ):
        raise ValueError("seat_numbers must be a list of strings")

    if not isinstance(flight_id, str):
        raise ValueError("flight_id must be str")

    for seat in seat_numbers:
        yield seat + flight_id + (12 - len(seat + flight_id)) * "0"
