"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    if not isinstance(student_scores, list):
        raise TypeError("student_scores must be a list")

    rounded_scores = []
    for score in student_scores:
        if isinstance(score, (int, float)):
            rounded_scores.append(round(score))
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    if not isinstance(student_scores, list):
        raise TypeError("student_scores must be a list")

    count = 0
    for score in student_scores:
        if isinstance(score, (int, float)) and score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    if not isinstance(student_scores, list):
        raise TypeError("student_scores must be a list")

    high_scores = []
    for score in student_scores:
        if isinstance(score, (int, float)) and score >= threshold:
            high_scores.append(score)
    return high_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    if not isinstance(highest, int) and highest <= 40:
        raise TypeError("highest must be an integer greater than 40")

    grade_thresholds = []
    increment = (highest - 40) // 4
    for i in range(4):
        grade_thresholds.append(41 + increment * i)
    return grade_thresholds


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    if (
        not isinstance(student_scores, list)
        or not isinstance(student_names, list)
        or len(student_scores) != len(student_names)
    ):
        raise TypeError(
            """
            student_scores must be a list must be a list of ints or floats
            and student_names must be a list of strings of the same length
            """
        )

    student_rankings = []
    for index, score in enumerate(student_scores):
        if isinstance(score, (int, float)):
            student_rankings.append(f"{index + 1}. {student_names[index]}: {score}")
    return student_rankings


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    if not isinstance(student_info, list):
        raise TypeError("student_info must be a list")

    for student, score in student_info:
        if (
            isinstance(student, str)
            and isinstance(score, (int, float))
            and score == 100
        ):
            return [student, score]
    return []
