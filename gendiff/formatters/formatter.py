from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def apply_formatter(diff_tree, formatter_name):
    if formatter_name == 'stylish':
        return render_stylish(diff_tree)
    if formatter_name == 'plain':
        return render_plain(diff_tree)
    if formatter_name == 'json':
        return render_json(diff_tree)
    raise Exception('Invalid format, choose from stylish, plain, json')
