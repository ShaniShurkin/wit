from wit import Wit


class WitInterface:
    @staticmethod
    def handle_commands(command, args):

        match args:
            case "init":
                Wit.init()
            case "add":
                Wit.add("temp1")
            case "commit":
                Wit.commit()
