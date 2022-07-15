import sys

from constant import *
from parser import *


# TODO: Needs argument handling
def main(argv):
    parser = Parser()
    parser.parse(argv[1], argv[2])


# Entry point
if __name__ == '__main__':
    main(sys.argv)
