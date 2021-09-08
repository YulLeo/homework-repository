def is_armstrong(number: int) -> bool:
    iterable_num = str(number)
    power = len(iterable_num)
    return number == sum(int(i)**power for i in iterable_num)
