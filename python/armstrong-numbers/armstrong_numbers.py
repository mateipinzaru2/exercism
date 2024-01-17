def is_armstrong_number(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")
    digits = [int(digit) for digit in str(number)]
    return sum([digit ** len(digits) for digit in digits]) == number
