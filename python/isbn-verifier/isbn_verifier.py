def is_valid(isbn):
    isbn_string = isbn.replace("-", "")

    if not isbn_string[:-1].isdecimal() or len(isbn_string) != 10:
        return False

    total = 0
    for i, num in enumerate(isbn_string[:-1]):
        total += int(num) * (10 - i)
    if isbn_string[-1].upper() == "X":
        total += 10
    elif isbn_string[-1].isdecimal():
        total += int(isbn_string[-1])
    else:
        return False
    return total % 11 == 0
