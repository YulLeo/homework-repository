import hashlib
import random
import struct
import time
from typing import Callable


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def time_meter(func: Callable) -> Callable:
    """Returns how many seconds took function execution"""
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        return time.time() - t1
    return wrapper
