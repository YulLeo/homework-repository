"""
Task 2
Here's a not very efficient calculation function that
calculates something important. Calculate total sum of
slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""

from multiprocessing import Pool


def hurry_up_slow_calculate(slow_func, args):
    """Makes slow_calculate function faster
    and calculate total sum of slow_calculate()
    """
    with Pool(500) as p:
        return sum(p.map(slow_func, args))