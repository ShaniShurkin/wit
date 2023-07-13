import pytest
from files_handler import FileHandler
from wit_exception import WitException


class TestFileHandler:
    def test_base_path(self):
        with pytest.raises(WitException):
            FileHandler.base_path
