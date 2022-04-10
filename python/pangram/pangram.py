from string import ascii_lowercase


def is_pangram(sentence):
    alphabet = set(ascii_lowercase)
    result = all([(letter in sentence.lower()) for letter in alphabet])
    return result
