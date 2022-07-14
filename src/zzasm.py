import sys

import constant
import parser


# TODO: Needs argument handling
def main(argv):
    p = parser.Parser()
    p.parse(argv[1], argv[2])


# Entry point
if __name__ == '__main__':
    main(sys.argv)
