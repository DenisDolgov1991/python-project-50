from gendiff.diff import generate_diff
from gendiff.formatters.plain import plain


def test_gendiff_json():
    file1_path = '.tests/fixtures/file1.json'
    file2_path = '.tests/fixtures/file2.json'
    result = generate_diff(file1_path, file2_path)
    output = open('.tests/fixtures/result.txt')

    assert result == output.read()

def test_gendiff_yaml():
    file1_path = '.tests/fixtures/file1.yaml'
    file2_path = '.tests/fixtures/file2.yaml'
    result = generate_diff(file1_path, file2_path)
    output = open('.tests/fixtures/result.txt')

    assert result == output.read()


def test_gendiff_nested_json():
    file1_path = '.tests/fixtures/file1_tree.json'
    file2_path = '.tests/fixtures/file2_tree.json'
    result = generate_diff(file1_path, file2_path)
    output = open('.tests/fixtures/result_nested.txt')

    assert result == output.read()


def test_gendiff_nested_yaml():
    file1_path = '.tests/fixtures/file1_tree.yaml'
    file2_path = '.tests/fixtures/file2_tree.yaml'
    result = generate_diff(file1_path, file2_path)
    output = open('.tests/fixtures/result_nested.txt')

    assert result == output.read()


def test_gendiff_plain():
    file1_path = '.tests/fixtures/file1_tree.json'
    file2_path = '.tests/fixtures/file2_tree.json'
    result = generate_diff(file1_path, file2_path, format=plain)
    output = open('.tests/fixtures/result_plain.txt')

    assert result == output.read()
