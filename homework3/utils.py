import time
import struct
import random
import hashlib


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def meter(f):
    def wrapper(*a, **kwargs):
        t1 = time.time()
        res = f(*a, **kwargs)
        return time.time() - t1
    return wrapper
