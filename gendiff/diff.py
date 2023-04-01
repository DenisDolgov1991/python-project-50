__all__ = ['generate_diff']

import os
from gendiff.parser import parse
from gendiff.difference import build_diff_tree
from gendiff.formatters.formatter import apply_formatter


def get_content(file_path):
    _, extension = os.path.splitext(file_path)
    with open(f'{file_path}') as input:
        return parse(input, extension[1:])


def generate_diff(file_path1, file_path2, format='stylish'):
    content1, content2 = map(get_content, (file_path1, file_path2))
    diff_tree = build_diff_tree(content1, content2)
    return apply_formatter(diff_tree, format)
