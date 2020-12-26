def classify(number):
    aliquot_sum = sum([i for i in range(1, number + 1) if number % i == 0])
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
