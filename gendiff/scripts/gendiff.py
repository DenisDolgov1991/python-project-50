#!/usr/bin/env python3

from gendiff.cli import parse_arguments
from gendiff.diff import generate_diff


def main():
    arguments = parse_arguments()
    diff = generate_diff(
        arguments.first_file,
        arguments.second_file,
        arguments.format
    )

    print(diff)


if __name__ == '__main__':
    main()
