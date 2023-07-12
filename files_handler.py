import os
import shutil


class FileHandler:
    _working_directory = None
    _base_path = None

    @classmethod
    @property
    def base_path(cls):
        if not cls._base_path:
            cls._base_path = cls.find_wit_dir()
        return cls._base_path

    @classmethod
    @property
    def working_directory(cls):
        if not cls._working_directory:
            cls._working_directory = os.getcwd()
        return cls._working_directory

    @staticmethod
    def create_dir(path):
        os.makedirs(path)

    @staticmethod
    def walk_up(path, top):
        while True:
            yield path
            if path == top:
                raise StopIteration
            else:
                path = os.path.dirname(path)

    @classmethod
    def find_wit_dir(cls):
        for p in cls.walk_up(os.path.dirname(cls.working_directory), "C:\\"):
            p = os.path.join(p, ".wit")
            if cls.create_and_validate_path(p, ".wit"):
                return p

        # TODO raise exception init wit before

    @classmethod
    def create_and_validate_path(cls, routing_end, routing_start=None):
        print("1")
        if not routing_start:
            print(2)
            routing_start = cls.working_directory
            print(cls.working_directory)
        print(f"routing_start: {routing_start}, type: {type(routing_start)}/n routing_end: {routing_end}, type: {type(routing_end)}")
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
            shutil.copytree(origin, target)
