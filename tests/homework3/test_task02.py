from homework3.task02 import hurry_up_slow_calculate
from homework3.utils import meter, slow_calculate


def test_hurry_up_slow_calculate():
    args = [i for i in range(0, 500)]
    assert meter(hurry_up_slow_calculate)(slow_calculate, args) < 60
