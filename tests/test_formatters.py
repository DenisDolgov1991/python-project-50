from gendiff.diff import generate_diff
import json
import pytest
from tests import get_full_path


@pytest.mark.parametrize('input1, input2, format, expected', [
    ('file1_tree.json', 'file2_tree.json',
        'plain', 'result_plain_tree.txt'),
    ('file1_tree.yaml', 'file2_tree.yaml',
        'plain', 'result_plain_tree.txt'),
    ('file1.json', 'file2.json', 'plain', 'result_plain.txt'),
        ('file1.yaml', 'file2.yaml', 'plain', 'result_plain.txt')
])
def test_generate_diff_in_plain_format(input1, input2, format, expected):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2, format)
    with open(f'{get_full_path(expected)}') as correct:
        assert result == correct.read()

@pytest.mark.parametrize('input1, input2, format', [
    ('file1_tree.json', 'file2_tree.json', 'json'),
    ('file1_tree.yaml', 'file2_tree.yaml', 'json')

def test_generate_diff_in_json_format(input1, input2, format):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2, format)

    assert json.loads(result)


@pytest.mark.parametrize('input1, input2, format', [
    ('file1_tree.yaml', 'file2_tree.yaml', 'style'),
    ('file1_tree.json', 'file2_tree.json', 'pain'),
    ('file1_tree.yaml', 'file2_tree.yaml', 'JSON')
])


def test_exception_in_generate_diff_in_wrong_format(input1, input2, format):
    file1, file2 = map(get_full_path, (input1, input2))
    with pytest.raises(Exception) as e:
        generate_diff(file1, file2, format)
    assert str(e.value) == 'Invalid format, choose from stylish, plain, json'
