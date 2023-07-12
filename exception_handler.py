import logging
import os
from functools import partial
from logger import Logger


def exception_handler(func):
    err_logger = partial(Logger.log_to, level=logging.ERROR)

    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except FileExistsError as ffe:
            err_logger(ffe)
        except Exception as e:
            err_logger(e)

    return inner_function
