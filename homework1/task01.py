def check_power_of_2(a: int) -> bool:
    """Returns if the given integer is a power of 2"""
    return a != 0 and not (bool(a & (a - 1)))
