from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import render_json


def apply_formatter(diff_tree, formatter_name):
    if formatter_name == 'stylish':
        return stylish(diff_tree)
    if formatter_name == 'plain':
        return plain(diff_tree)
    if formatter_name == 'json':
        return render_json(diff_tree)
    raise Exception('Invalid format, choose from stylish, plain, json')
