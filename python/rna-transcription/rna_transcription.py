"""
Determines the RNA complement of a given DNA sequence.
"""


def to_rna(dna_strand: str) -> str:
    """
    Returns the RNA complement of a given DNA sequence.

    Input:
        dna_strand: string

    output:
        rna_strand: string
    """

    if not isinstance(dna_strand, str):
        raise TypeError("dna_strand must be a string")

    trans = str.maketrans("GCTA", "CGAU")
    rna_strand = dna_strand.translate(trans)

    return rna_strand
