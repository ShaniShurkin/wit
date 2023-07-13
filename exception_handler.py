import logging
import os
from functools import partial
from logger import Logger
from wit_exception import WitException


def exception_handler(func):
    err_logger = partial(Logger.log_to, level=logging.ERROR)
    #, traceback = True
    def inner_function(*args, **kwargs):
        try:
            func_res = func(*args, **kwargs)
            return func_res
        except FileExistsError as ffe:
            err_logger(str(ffe))
        except WitException as we:
            err_logger(str(we))
        except Exception as e:
            err_logger(str(e))

    return inner_function
