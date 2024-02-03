""" https://exercism.org/tracks/python/exercises/anagram """


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    Extracts anagrams based on target words and list of candidates

    Args:
        word: string representing an English word
        candidates: list of strings representing potential anagrams

    Returns:
        output: subset of candidates that represent valid anagrams of target word
    """

    return [
        anagram
        for anagram in candidates
        if anagram.casefold() != word.casefold()
        and sorted(anagram.casefold()) == sorted(word.casefold())
    ]
