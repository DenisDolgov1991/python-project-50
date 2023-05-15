from gendiff.difference import ADDED, DELETED, UPDATED


DOT = '.'


def get_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, int):
        return value
    return f"'{str(value)}'"


def render_plain(difference_dict, path=''):
    lines = []

    for key, diff_info in difference_dict.items():
        value = diff_info.get('value')
        status = diff_info.get('status')

        if status == ADDED:
            value = get_to_str(value)
            lines.append(
                f"Property '{path + key}' was added with value: {value}"
            )

        elif status == DELETED:
            lines.append(
                f"Property '{path + key}' was removed"
            )

        elif status == UPDATED:
            value1, value2 = map(get_to_str, value)
            item = path + key

            lines.append(
                f"Property '{item}' was updated. From {value1} to {value2}"
            )

        elif isinstance(value, dict):
            lines.append(render_plain(value, path + key + DOT))

    return '\n'.join(lines)
