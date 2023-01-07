def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    number_of_steps = 0
    while number > 1:
        number = number / 2 if number % 2 == 0 else 3 * number + 1
        number_of_steps += 1
    return number_of_steps
