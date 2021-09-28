from homework3.task02 import hurry_up_slow_calculate
from homework3.utils import slow_calculate, time_meter


def test_hurry_up_slow_calculate():
    args = [num for num in range(0, 500)]
    assert time_meter(hurry_up_slow_calculate)(slow_calculate, args) < 60
