def backspace_compare(first: str, second: str) -> bool:
    """
    Returns if strings are equal when both are typed into
    empty text editors.
    '#'means a backspace character.
    """
    first_input = ''.join(
        char
        for numb, char in enumerate(first)
        if first[numb + 1: numb + 2] != '#' and char != '#'
    )
    second_input = ''.join(
        char
        for numb, char in enumerate(second)
        if second[numb + 1: numb + 2] != '#' and char != '#'
    )
    return first_input == second_input
