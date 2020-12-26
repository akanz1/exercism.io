def is_isogram(string):
    str_lower = string.lower()
    return all(str_lower.count(char) == 1 for char in str_lower if char.isalpha())
