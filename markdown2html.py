#!/usr/bin/python3
''' a script that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
'''
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
    else:
        exit(0)
