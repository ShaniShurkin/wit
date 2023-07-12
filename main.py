from wit_interface import WitInterface
import sys



if __name__ == '__main__':
    main_arg = sys.argv[1]
    WitInterface.handle_commands(0, main_arg)


