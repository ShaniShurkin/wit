import os
import shutil


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

    @staticmethod
    def create_dir(path):
        os.mkdir(path)

    @classmethod
    def find_base_dir(cls):
        for root, dirs, files in os.walk(cls.working_directory, topdown=False):
            for name in dirs:
                if name == ".wit":
                    return os.path.join(root, name)
        return None
        # TODO raise exception init wit before

    @classmethod
    def get_full_path(cls, routing_end, routing_start=None):
        if not routing_start:
            routing_start = cls.working_directory
        full_path = os.path.join(routing_start, routing_end)
        return full_path
        # print(full_path)
        # if not os.path.exists(full_path):
        #     pass
        # TODO: handle file doesn't exist


    @classmethod
    def copy_item(cls, origin, target):
        if os.path.isfile(origin):
            
            shutil.copy(origin, target)
        else:
            target = os.path.join(target, os.path.basename(os.path.normpath(origin)))
            shutil.copytree(origin, target)
