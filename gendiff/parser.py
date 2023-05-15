import os
import json
import yaml


def open_json(path):
    return json.load(path)


def open_yaml(path):
    return yaml.safe_load(path)


def parse(content, format_name):
    if format_name == 'json':
        return open_json(content)
    if format_name == 'yaml' or format_name == 'yml':
        return open_yaml(content)
    raise Exception('Comparison is available only for json and yaml files')


def get_content(file_path):
    _, extension = os.path.splitext(file_path)
    file_format = extension[1:]
    with open(file_path) as input:
        return parse(input, file_format)
