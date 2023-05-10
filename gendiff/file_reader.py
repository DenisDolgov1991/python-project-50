import os

from gendiff import parser


def get_content(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as input:
        return parse(input, extension[1:])
