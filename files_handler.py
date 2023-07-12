import os
import shutil
from exception_handler import exception_handler
from logger import Logger
import logging


class FileHandler:
    _working_directory = None
    _base_path = None

    @classmethod
    @property
    def base_path(cls):
        cls._base_path = cls.find_base_dir()
        return cls._base_path

    @classmethod
    @property
    def working_directory(cls):
        if not cls._working_directory:
            cls._working_directory = os.getcwd()
        return cls._working_directory

    @classmethod
    def create_dir(cls, path):
        os.mkdir(path)
        message = f"A new folder {os.path.basename(os.path.normpath(path))} was created in the path: {path}"
        Logger.log_to(level=logging.INFO, message=message)

    @classmethod
    def find_base_dir(cls):
        for root, dirs, files in os.walk(cls.working_directory, topdown=False):
            for name in dirs:
                if name == ".wit":
                    return os.path.join(root, name)
        else:
            Logger.log_to(level=logging.ERROR, message="There is no .wit directory in project")
            return None
            # TODO raise excption init wit before

    @exception_handler
    @classmethod
    def get_full_path(cls, routing_end, routing_start=None):
        if not routing_start:
            routing_start = cls.working_directory
        full_path = os.path.join(routing_start, routing_end)
        if not os.path.exists(full_path):
            message = f"No such path exists: {full_path}"
            raise FileExistsError(message)
        return full_path

    @classmethod
    def copy_item(cls, origin, target):
        if os.path.isfile(origin):
            shutil.copy(origin, target)
        else:
            target = os.path.join(target, os.path.basename(os.path.normpath(origin)))

            shutil.copytree(origin, target)
        Logger.log_to(level=logging.INFO, message=f"An item has been copied from {origin} to {target}")
        # except FileExistsError as fee:
        #     Logger.log_to(level=logging.ERROR, message=fee)
        # except Exception as e:
        #     Logger.log_to(level=logging.ERROR, message=e)


FileHandler.get_full_path("g\\", "y\\j")
