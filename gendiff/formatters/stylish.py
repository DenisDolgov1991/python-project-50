import itertools

from gendiff.difference import ADDED, DELETED, UPDATED


ADD = '  + '
DEL = '  - '
SP = '    '


def get_to_str(value, level):
    if isinstance(value, dict):
        return render_stylish(value, level)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def render_stylish(diff_dict, level=0):
    current_indent = SP * level
    lines = []

    for key, diff_info in diff_dict.items():
        value = diff_info if not isinstance(diff_info, dict) \
            else diff_info.get('value', diff_info)
        status = '' if not isinstance(diff_info, dict) \
            else diff_info.get('status')

        if status == ADDED:
            lines.append(
                f'{current_indent}{ADD}{key}: {get_to_str(value, level + 1)}'
            )
        elif status == DELETED:
            lines.append(
                f'{current_indent}{DEL}{key}: {get_to_str(value, level + 1)}'
            )
        elif status == UPDATED:
            value1, value2 = value
            lines.append(
                f'{current_indent}{DEL}{key}: {get_to_str(value1, level + 1)}'
            )
            lines.append(
                f'{current_indent}{ADD}{key}: {get_to_str(value2, level + 1)}'
            )
        else:
            lines.append(
                f'{current_indent}{SP}{key}: {get_to_str(value, level + 1)}'
            )

    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
