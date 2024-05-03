import time
from functools import wraps

from loguru import logger


# Decorador de medida de tempo
def time_measure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(
            f"Função '{func.__name__}' executada em {end_time - start_time:.4f} segundos"
        )
        return result

    return wrapper
