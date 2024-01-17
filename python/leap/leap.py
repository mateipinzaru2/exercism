def leap_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
