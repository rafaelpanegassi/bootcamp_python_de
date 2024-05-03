from loguru import logger

logger.add("info.log")


def soma(x, y):
    logger.info(x)
    logger.info(y)
    return x + y


soma(2, 3)
