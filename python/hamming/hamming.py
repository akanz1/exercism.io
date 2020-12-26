def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(
            "Hamming distance is only defined for strings of equal length."
        )
    return sum([a != b for a, b in zip(strand_a, strand_b)])
