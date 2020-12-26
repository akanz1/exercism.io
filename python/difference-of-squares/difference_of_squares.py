def square_of_sum(number):
    return sum(range(number + 1)) ** 2


def sum_of_squares(number):
    result = sum(x ** 2 for x in range(number + 1))
    return result


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
