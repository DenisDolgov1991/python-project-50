import os

import json
import yaml


def parse(content, format_name):
    if format_name == 'json':
        return json.load(content)
    if format_name == 'yaml' or format_name == 'yml':
        return yaml.safe_load(content)
    raise Exception('Comparison is available only for json and yaml files')


def get_content(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as input:
        return parse(input, extension[1:])
