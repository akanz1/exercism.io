translation = {
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
}
stop = ["UAA", "UAG", "UGA"]


def proteins(strand):
    result = []
    codon_list = [strand[i : i + 3] for i in range(0, len(strand), 3)]
    for codon in codon_list:
        if codon in stop:
            break
        for key in translation.keys():
            codon = codon.replace(key, translation[key])
        result.append(codon)
    return result
