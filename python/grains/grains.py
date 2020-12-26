def square(number):
    if not 0 < number <= 64:
        raise ValueError("Square out of range.")
    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1
