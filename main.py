from wit_interface import WitInterface
import sys



if __name__ == '__main__':
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)


