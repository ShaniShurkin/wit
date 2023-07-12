import logging
import os

from files_handler import FileHandler
from logger import Logger

class Wit:
    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.base_path

    @staticmethod
    def init():
        print(Wit.validate_is_wit_repo())
        if not Wit.validate_is_wit_repo() is None:
            raise FileExistsError("this repository had already init")
        else:
            FileHandler.create_dir("./.wit")
            FileHandler.create_dir("./.wit/images")
            FileHandler.create_dir("./.wit/staging_area")
            message = f"init successful"
            Logger.log_to(level=logging.INFO, message=message)

    @staticmethod
    def move_to_staging(source_path):
        target_path = FileHandler.get_full_path("staging_area", FileHandler.base_path)
        FileHandler.copy_item(source_path, target_path)

    @staticmethod
    def add(args):
        full_path = FileHandler.get_full_path(args[0])
        Wit.move_to_staging(full_path)
        message = f"add successful"
        Logger.log_to(level=logging.INFO, message=message)

    @staticmethod
    def commit():
        pass
