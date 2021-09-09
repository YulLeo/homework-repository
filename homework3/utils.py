import hashlib
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def meter(f):
    """Returns how many seconds took function execution"""
    def wrapper(*a, **kwargs):
        t1 = time.time()
        f(*a, **kwargs)
        return time.time() - t1
    return wrapper
