from homework3.utils import meter
from homework3.utils import slow_calculate
from homework3.task02 import hurry_up_slow_calculate


def test_hurry():
    args = [i for i in range(0, 500)]
    assert meter(hurry_up_slow_calculate)(slow_calculate, args) < 60

