import logging
import os
from functools import partial

from exception_handler import exception_handler
from files_handler import FileHandler
from logger import Logger
from wit_exception import WitException


class Wit:
    _wit_dir = None
    _info_logger = partial(Logger.log_to, level=logging.INFO)
    @classmethod
    def validate_is_wit_repo(cls):
        return cls._wit_dir is not None

    @classmethod
    @exception_handler
    def init(cls):
        if not cls.validate_is_wit_repo() is None:
            raise WitException("this repository had already init")
        else:
            FileHandler.create_dir("./.wit")
            FileHandler.create_dir("./.wit/images")
            FileHandler.create_dir("./.wit/staging_area")
            message = f"init successful"
            cls._info_logger(message)
            cls._wit_dir = FileHandler.base_path

    @classmethod
    @exception_handler
    def move_to_staging(cls, source_path):
        if not cls.validate_is_wit_repo():
            cls._wit_dir = FileHandler.base_path
        target_path = FileHandler.get_full_path("staging_area", cls._wit_dir)
        FileHandler.copy_item(source_path, target_path)

    @classmethod
    @exception_handler
    def add(cls, args):
        full_path = FileHandler.get_full_path(args[0])
        Wit.move_to_staging(full_path)
        message = f"add successful"
        cls._info_logger(message)

    @staticmethod
    def commit():
        pass
