"""Functions for creating, transforming, and adding prefixes to strings."""

import string


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    if not isinstance(word, str):
        raise TypeError("word must be a string")

    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    if not isinstance(vocab_words, list) and not (
        all(isinstance(word, str) for word in vocab_words)
    ):
        raise TypeError("vocab_words must be a list of strings")

    prefix = vocab_words[0]
    words = vocab_words[1:]
    words_with_prefix = [prefix + word for word in words]
    return prefix + " :: " + " :: ".join(words_with_prefix)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    if not isinstance(word, str):
        raise TypeError("word must be a string")

    if word.endswith("iness"):
        return word[:-5] + "y"
    if word.endswith("ness"):
        return word[:-4]
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    if not isinstance(sentence, str) or not isinstance(index, int):
        raise TypeError("sentence must be a string and index must be an int")

    words = sentence.split()
    adjective = words[index]
    if adjective[-1] in string.punctuation:
        return adjective[:-1] + "en"
    if adjective.endswith("e"):
        return adjective + "n"
    return adjective + "en"
