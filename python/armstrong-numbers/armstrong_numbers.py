def is_armstrong_number(number):
    length = len(str(number))
    result = sum([int(digit) ** length for digit in str(number)])
    return result == number
