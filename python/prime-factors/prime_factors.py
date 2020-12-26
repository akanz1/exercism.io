def factors(value):
    factors, factor = [], 2
    while value > 1:
        while value % factor == 0:
            value /= factor
            factors.append(factor)
        factor += 1
    return factors
