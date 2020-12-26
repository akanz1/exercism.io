color_list = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    code = [str(color_list.index(color)) for color in colors[:2]]
    code = "".join(code)
    return int(code)
