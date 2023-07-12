import logging
import os
from functools import partial
from logger import Logger


def exception_handler(func):
    err_logger = partial(Logger.log_to, level=logging.ERROR)

    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except FileExistsError:
            message = f"The folder {os.path.basename(os.path.normpath(path))} already exists in the path: {path}"
            err_logger(message)
        except Exception as e:
            message = f"An error occurred while creating the folder: {str(e)}"
            err_logger(message)

    return inner_function
