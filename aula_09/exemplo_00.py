from hello import hello
from log import log_decorator
from timer import time_measure_decorator


@hello
def soma_1(a, b):
    return a + b


soma_1(1, 2)
