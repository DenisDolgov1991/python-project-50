#!/usr/bin/env python3

from gendiff.cli import parse_arguments
from gendiff.diff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


args = parse_arguments()


def main():
    if args.format == 'plain':
        diff = generate_diff(args.first_file, args.second_file, format=plain)
    else:
        diff = generate_diff(args.first_file, args.second_file, format=stylish)

    print(diff)


if __name__ == '__main__':
    main()
