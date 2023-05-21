def triplets_with_sum(number: int) -> list:
    result = []

    for c in range(int(number * (2**0.5 - 1)), number // 2):
        a_plus_b = number - c
        for b in range(a_plus_b // 2 + 1, a_plus_b):
            a = a_plus_b - b
            if a < b < c and is_triplet(a, b, c):
                result.append([a, b, c])
    return result


def is_triplet(a: int, b: int, c: int) -> bool:
    return a**2 + b**2 == c**2
