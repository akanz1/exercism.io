def translate(text):
    new_text = []
    split = text.split()
    for word in split:
        if word.startswith(("a", "e", "i", "o", "u", "xr", "yt")):
            new_text.append(f"{word}ay")
        elif word.startswith(("sch", "thr", "squ")):
            new_text.append(word[3:] + word[:3] + "ay")
        elif word.startswith(("ch", "qu", "th", "yt", "rh")):
            new_text.append(word[2:] + word[:2] + "ay")
        else:
            new_text.append(word[1:] + word[:1] + "ay")
    return " ".join(new_text)
