import logging
import sys
import traceback


class TracebackFormatter(logging.Formatter):
    def formatException(self, exc_info):
        exception_text = super().formatException(exc_info)
        traceback_text = "".join(traceback.format_tb(exc_info[2]))
        return f"{exception_text}\n{traceback_text}"


class Logger:
    _level = logging.INFO
    _format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
    _filename = "logger.txt"

    logging.basicConfig(format=_format, level=_level)
    _logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler(_filename)
    # file_formatter = TracebackFormatter(_format)
    # file_handler.setFormatter(file_formatter)
    _logger.addHandler(file_handler)

    @classmethod
    def log_to(cls, message, level=logging.INFO, traceback=False):
        if level == logging.ERROR and traceback:
            exc_info = sys.exc_info()
            cls._logger.log(level=level, msg=message, exc_info=exc_info)
        else:
            cls._logger.log(level=level, msg=message)

    # @classmethod
    # @property
    # def logger(cls):
    #     return cls._logger

    # @classmethod
    # @logger.setter
    # def logger(cls, level=logging.INFO, format="MSG: %(message)s"):
    #     cls._level = level
    #     cls._format = format
    #     logging.basicConfig(format=format, level=level)
