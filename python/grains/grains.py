def square(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError("square must be an integer.")
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total() -> int:
    return (2**64) - 1
