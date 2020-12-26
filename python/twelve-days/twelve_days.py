def recite(start_verse, end_verse):
    recite_list = [
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
    ]
    days = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]
    if end_verse == 1:
        recite_list[0] = "a Partridge in a Pear Tree."
    begin = [f"On the {days[end_verse - 1]} day of Christmas my true love gave to me: "]

    if start_verse == end_verse:
        for i in reversed(range(end_verse)):
            begin.append(recite_list[i])
    else:
        for i in reversed(range(start_verse - 1, end_verse)):
            begin.append(recite_list[i])

    begin = ["".join(begin)]
    return begin