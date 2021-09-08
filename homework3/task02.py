from multiprocessing import Pool


def hurry_up_slow_calculate(slow_func, args):
    """Makes slow_calculate function faster"""
    with Pool(500) as p:
        return sum(p.map(slow_func, args))
