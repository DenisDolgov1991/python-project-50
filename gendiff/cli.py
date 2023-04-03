import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration file and shows a difference'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', 
        default=stylish, choices=['stylish', 'plain', 'json'],
        help='set format of output'
    )
    return parser.parse_args()
