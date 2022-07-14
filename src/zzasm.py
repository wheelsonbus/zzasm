import sys

import constant
import parser


# TODO: Needs argument handling
def main(argv):
    p = parser.Parser(argv[1])
    p.run()

# Entry point
if __name__ == '__main__':
    main(sys.argv)
