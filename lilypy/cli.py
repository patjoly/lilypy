#!/usr/bin/env python
import argparse
from lilypy.commands import new_file, convert_file

def main():
    parser = argparse.ArgumentParser(prog='lilypy')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # new command
    new_parser = subparsers.add_parser('new', help='Create a new lilypond file')
    new_parser.add_argument('--instrument', required=True)
    new_parser.add_argument('--key', default='c')
    new_parser.add_argument('--mode', default='major')
    new_parser.add_argument('--title', default='Untitled')
    new_parser.add_argument('--composer', default='')
    new_parser.add_argument('--arranger', default='')
    new_parser.add_argument('--output', required=True)
    new_parser.add_argument(
        "--concert",
        action="store_true",
        help="Include concert pitch staff (if supported)"
    )

    # convert command
    convert_parser = subparsers.add_parser('convert', help='Convert notation')
    convert_parser.add_argument('--mode', choices=['relative'], required=True)
    convert_parser.add_argument('file')

    args = parser.parse_args()

    if args.command == 'new':
        new_file(args)

    elif args.command == 'convert':
        convert_file(args)

if __name__ == "__main__":
    main()

