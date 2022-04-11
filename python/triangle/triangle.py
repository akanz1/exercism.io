def equilateral(sides):
    return sides[0] == sides[1] == sides[2] if sides[0] > 0 else False


def isosceles(sides):
    return (
        sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
        if _is_valid_triangle(sides)
        else False
    )


def scalene(sides):
    return (
        not equilateral(sides) and not isosceles(sides)
        if _is_valid_triangle(sides)
        else False
    )


def _is_valid_triangle(sides):
    return sum(sides) > 2 * max(sides)
