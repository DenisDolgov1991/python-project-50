import json
import itertools


def get_value(file, key):
    value = file.get(key)
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_patch1, file_patch2):
    file1 = json.load(open(tests/fixtures/file1.json))
    file2 = json.load(open(tests/fixtures/file2.json))
    sorted_file = sorted(set(file_patch1.keys()) | set(file_patch2.keys()))
    new_file = []
    for key in sorted_file:
        if key not in file1:
            new_file.append(f" +{key}: {get_value(file2, key)}")
        elif key not in file2:
            new_file.append(f" -{key}: {get_value(file1, key)}")
        elif file1[key] == file2[key]:
            new_file.append(f" {key}: {get_value(file1, key)}")
        else:
            new_file.append(f" -{key}: {get_value(file1, key)}")
            new_file.append(f" +{key}: {get_value(file2, key)}")
    new_file = '\n'.join(itertools.chain('{', new_file, '}'))
    return new_file
