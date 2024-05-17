def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    vector = sorted([a, b, c])
    return vector[1]
