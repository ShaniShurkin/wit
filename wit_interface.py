from wit import Wit


class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        match command:
            case "init":
                Wit.init()
            case "add":
                Wit.add(args)
            case "commit":
                Wit.commit()

