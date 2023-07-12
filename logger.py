import logging


class Logger:
    _level = logging.INFO
    _format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
    logging.basicConfig(format=_format, level=_level, filename="logger.txt")
    _logger = logging.getLogger(__name__)

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

    @classmethod
    def log_to(cls, message, level=logging.INFO):
        cls._logger.log(level=level, msg=message)


