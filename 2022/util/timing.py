from functools import wraps
from time import time


def timeit(f):
    """Print the execution time of a function"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        ts = time()
        result = f(*args, *kwargs)
        te = time()
        print(f"completed in {(te - ts) * 10**3} ms")
        return result

    return wrapper