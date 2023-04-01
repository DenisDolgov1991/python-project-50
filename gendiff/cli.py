import argparse
from gendiff.formatters.stylish import stylish

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration and shows a difference'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default=stylish, help='set format of output')

    return parser.parse_args()
