import os

from files_handler import FileHandler


class Wit:
    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.base_path

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            # TODO: message this repository had already init
            pass
        else:
            FileHandler.create_dir("./.wit")
            FileHandler.create_dir("./.wit/images")
            FileHandler.create_dir("./.wit/staging_area")

    @staticmethod
    def move_to_staging(source_path):
        target_path = FileHandler.create_and_validate_path(FileHandler.base_path, "staging_area")
        FileHandler.copy_item(source_path, target_path)

    @staticmethod
    def add(*args):
        full_path = FileHandler.create_and_validate_path(routing_end=args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit():
        pass

