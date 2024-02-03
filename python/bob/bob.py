"""
Bob is a lackadaisical teenager. In conversation, his responses are very limited.
Bob answers 'Sure.' if you ask him a question, such as "How are you?".
He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.
"""


def response(hey_bob: str) -> str:
    """Bob's response to a given statement."""

    stripped = hey_bob.strip()

    if stripped == "":
        return "Fine. Be that way!"
    if stripped.isupper() and stripped.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if stripped.isupper():
        return "Whoa, chill out!"
    if stripped.endswith("?"):
        return "Sure."
    return "Whatever."
