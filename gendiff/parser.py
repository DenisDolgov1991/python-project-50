import os
import json
import yaml


def open_json(path):
    return json.load(path)


def open_yaml(path):
    return yaml.safe_load(path)


DICT_FORMAT = {'yaml': open_yaml, 'yml': open_yaml, 'json': open_json}


def get_content(file_path):
    path, extension = os.path.splitext(file_path)
    file_format = extension[1:]
    if file_format not in DICT_FORMAT:
        return ''
    with open(file_path) as path:
        return DICT_FORMAT[file_format](path)
