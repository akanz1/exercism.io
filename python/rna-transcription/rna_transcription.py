dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand):
    result = ""
    for char in dna_strand:
        result += char.replace(char, dna_to_rna[char])
    return result
