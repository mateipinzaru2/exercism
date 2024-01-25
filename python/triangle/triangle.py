def is_triangle(sides: list) -> bool:
    if not (
        isinstance(sides, list)
        and len(sides) == 3
        and all(isinstance(side, (int, float)) and side > 0 for side in sides)
    ):
        return False

    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b


def equilateral(sides: list) -> bool:
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list) -> bool:
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: list) -> bool:
    return is_triangle(sides) and len(set(sides)) == 3
