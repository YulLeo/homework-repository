from homework11.task01 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ('RED', 'RED', 'BLUE', 'ORANGE', 'BLACK')


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ('XL', 'L', 'M', 'S', 'XS')


def test_simplified_enum_colors():
    assert ColorsEnum.BLUE == 'BLUE'


def test_simplified_enum_size():
    assert SizesEnum.M == 'M'


def test_simplified_enum_colors_duplicates():
    assert dir(ColorsEnum).count('RED') == 1