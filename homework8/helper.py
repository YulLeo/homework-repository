def clean_string(line: str) -> list:
    """
    Splits string into two variables by '=' char
    """
    line = line.strip().split('=', 1)
    for char in line:
        if char.isdigit():
            line[line.index(char)] = int(char)
    return line
