from string import ascii_lowercase


def rotate(text, key):
    encoded_text = ""
    for letter in text.lower():
        if letter.isalpha():
            encoded_text += ascii_lowercase[(ascii_lowercase.index(letter) + key) % 26]
        else:
            encoded_text += letter

    for i in range(len(text)):
        if text[i].isupper():
            encoded_text = encoded_text.replace(
                encoded_text[i], encoded_text[i].upper(), 1
            )

    return "".join(encoded_text)
