import os

from files_handler import FileHandler


class Wit:
    _wit_dir = None

    @classmethod
    def validate_is_wit_repo(cls):
        return cls._wit_dir is not None

    @classmethod
    def init(cls):
        if cls.validate_is_wit_repo():
            pass
            # TODO: message this repository had already init

        else:
            FileHandler.create_dir("./.wit")
            FileHandler.create_dir("./.wit/images")
            FileHandler.create_dir("./.wit/staging_area")
            cls._wit_dir = FileHandler.base_path

    @classmethod
    def move_to_staging(cls, source_path):
        if not cls.validate_is_wit_repo():
            cls._wit_dir = FileHandler.base_path
        target_path = FileHandler.get_full_path("staging_area", cls._wit_dir)
        FileHandler.copy_item(source_path, target_path)

    @staticmethod
    def add(args):
        full_path = FileHandler.get_full_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit():
        pass
