import os


class FileHandler:
    working_directory = None
    _base_path = None
    @staticmethod
    def create_dir(path):
        os.mkdir(path)

    @property
    def base_path(self):
        if not self.base_path:
            self._base_path = self.find_wit_dir()
        return self._base_path

    @staticmethod
    def find_working_dir():
        return os.getcwd()

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
        path = cls.find_working_dir()
        for p in cls.walk_up(os.path.dirname(path), "C:\\"):
            p = os.path.join(p, ".wit")
            if os.path.isdir(p):
                return p
        # TODO raise exception init wit before

    def walk_up(path, top):
        while True:
            yield path
            if path == top:
                raise StopIteration
            else:
                path = os.path.dirname(path)




    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            pass
            # TODO: handle file doesn't exist

    @classmethod
    def copy_item(cls, origin, target):
        pass
