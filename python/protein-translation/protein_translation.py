""" https://exercism.org/tracks/python/exercises/protein-translation """

from typing import Iterator


CODON_LENGTH = 3
STOP_CODON_PROTEIN = "STOP"
PROTEINS = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand: str) -> list[str]:
    """
    Translates RNA sequences into proteins.

    Args:
        strand: string indicating the RNA sequence to be transformed.

    Returns:
        proteins: list of strings indicating the corresponding proteins.
    """

    def generate_codons(strand: str) -> Iterator[str]:
        """
        Generates codons from the given RNA strand.

        Args:
            strand: string indicating the RNA sequence to be transformed.

        Yields:
            codons: substrings of the RNA sequence of length CODON_LENGTH.
        """

        for i in range(0, len(strand), CODON_LENGTH):
            if len(strand[i : i + CODON_LENGTH]) == CODON_LENGTH:
                yield strand[i : i + CODON_LENGTH]

    protein_sequence = []
    for codon in generate_codons(strand):
        if codon not in PROTEINS:
            continue
        if PROTEINS[codon] == STOP_CODON_PROTEIN:
            break
        protein_sequence.append(PROTEINS[codon])
    return protein_sequence
