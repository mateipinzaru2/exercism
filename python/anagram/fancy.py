""" https://exercism.org/tracks/python/exercises/anagram """

import nltk
from nltk.corpus import words

nltk.download("words")


def is_english_word(word) -> bool:
    """
    Checks if a word is a valid English word.

    Args:
        word: string indicating the word to be checked.

    Returns:
        is_valid: boolean indicating if the word is a valid English word.
    """

    word_list = words.words()
    return word.lower() in word_list


def word_to_dict(word: str) -> dict[str, int]:
    """
    Splits word in case-sensitive keys, each key representing a word's letter.
    Each key's value is the letter count (how many times it appears in the word).

    Args:
        word: a valid English word

    Returns:
        dict[str]: a dictionary made of the word's letters and their count
    """

    output = {}
    for char in word.lower():
        if char in output:
            output[char] += 1
        else:
            output[char] = 1
    return output


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    Extracts anagrams based on target words and list of candidates

    Args:
        word: string representing an English word
        candidates: list of strings representing potential anagrams

    Returns:
        output: subset of candidates that represent valid anagrams of target word
    """

    if not is_english_word(word):
        raise TypeError("word must be an English word")

    if not all(isinstance(candidate, str) for candidate in candidates):
        raise TypeError("candidates must be a list of words")

    output = []
    target = word_to_dict(word)

    for candidate in candidates:
        if candidate.lower() != word.lower():
            if word_to_dict(candidate) == target:
                output.append(candidate)

    return output
