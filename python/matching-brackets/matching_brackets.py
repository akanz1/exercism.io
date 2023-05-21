def is_paired(input_string: str) -> bool:
    braces = "{}"
    brackets = "[]"
    parentheses = "()"

    sanitized = "".join(
        c for c in input_string if c in ",".join([braces, brackets, parentheses])
    )

    while any([braces in sanitized, brackets in sanitized, parentheses in sanitized]):
        sanitized = sanitized.replace(braces, "")
        sanitized = sanitized.replace(brackets, "")
        sanitized = sanitized.replace(parentheses, "")

    return not sanitized
