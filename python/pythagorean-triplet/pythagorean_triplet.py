def triplets_with_sum(number):
    result = []

    for c in range(number // 2 + 1):
        a_plus_b = number - c
        for b in range(a_plus_b // 2, a_plus_b):
            a = a_plus_b - b
            if a < b < c:
                if is_triplet(a, b, c):
                    result.append([a, b, c])
    return result


def is_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2
