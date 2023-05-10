from gendiff.difference import build_diff_tree
from gendiff.formatters.formatter import apply_formatter
from gendiff.file_reader import get_content


def generate_diff(file_path1, file_path2, format='stylish'):
    content1, content2 = map(get_content, (file_path1, file_path2))
    diff_tree = build_diff_tree(content1, content2)

    return apply_formatter(diff_tree, format)
