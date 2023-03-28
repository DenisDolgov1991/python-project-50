#!/usr/bin/env python3

from gendiff.cli import parse_arguments
from gendiff.diff import generate_diff

def main():
    args = parse_arguments()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
