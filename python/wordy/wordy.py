""" 
Program that parses and evaluates simple math word problems returning the answer as an integer.
"""

from typing import Union


OPS = {
    "plus": "__add__",
    "minus": "__sub__",
    "multiplied by": "__mul__",
    "divided by": "__truediv__",
}


def answer(question: str) -> Union[int, ValueError]:
    """
    Parse and evaluate simple math word problems.
    The supported operations are addition, subtraction, multiplication and division.

    Args:
        question (str): the math word problem starting with "What is".

    Returns:
        int: the answer to the math word problem.
    """

    question = question.removeprefix("What is").removesuffix("?").strip()

    if not question:
        raise ValueError("syntax error")

    if question.isdigit():
        return int(question)

    found_op = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            found_op = True
    if not found_op:
        raise ValueError("unknown operation")

    output = question.split()
    while len(output) > 1:
        try:
            x, op, y, *tail = output
            if op not in OPS.values():
                raise ValueError("syntax error")
            output = [getattr(int(x), op)(int(y)), *tail]
        except Exception as exc:
            raise ValueError("syntax error") from exc

    return int(output[0])
