def sequence(length: int) -> str:
    if length < 1:
        return ""
    return "".join([str(number) for number in range(1, length + 1)])
