from gendiff.generate_diff import generate_diff
import pytest


file1 = './tests/fixtures/file_1.json'
file2 = './tests/fixtures/file_2.json'
result = '- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true'


def test_generate_diff():
    assert generate_diff(file1, file2) == result
