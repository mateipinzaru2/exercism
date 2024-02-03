import random
from protein_translation import (
    proteins,
)


def generate_rna_sequence(length):
    """
    Generates a random RNA sequence of the given length.

    Args:
        length: int indicating the length of the RNA sequence to be generated.

    Returns:
        rna_sequence: string indicating the generated RNA sequence.
    """

    rna_bases = ["A", "C", "G", "U"]
    return "".join(random.choice(rna_bases) for _ in range(length))


rna_sequence = generate_rna_sequence(10000)
print(rna_sequence)
print(proteins(rna_sequence))
