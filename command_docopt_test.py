import sys
from docopt import docopt

doc='''
Usage:
    my_program tcp <host> <port> [--timeout=<seconds>]
    my_program serial <port> [--baud=<n>] [--timeout=<seconds>]
    my_program (-h | --help | --version)

Options:
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
    --timeout=<seconds>  timeout [default: 50]
'''

def test(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = docopt(doc, argv=argv, version='0.01')
    print args

    pass


if __name__ == '__main__':
    test()