def backspace_compare(first: str, second: str) -> bool:
    """
    Returns if strings are equal when both are typed into
    empty text editors.
    '#'means a backspace character.
    """
    return string_without_backspace(first) == string_without_backspace(second)


def string_without_backspace(str_with_backspace: str) -> str:
    """
    Returns new string without backspace character
    """
    new_string = ''
    for numb, char in enumerate(str_with_backspace):
        if str_with_backspace[numb + 1: numb + 2] != '#' and char != '#':
            new_string += char
    return new_string
