import sys
from wit import Wit

class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        main_arg = sys.argv[1]
        match main_arg:
            case "init":
                Wit.init()
            case "add":
                Wit.add("temp1")
            case "commit":
                Wit.commit()