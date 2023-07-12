from wit_interface import WitInterface
import sys

if __name__ == '__main__':
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)


# TODO: change command to be wit instead of python main.py
# TODO: create flags if client wants to see logging (-d, -i)
