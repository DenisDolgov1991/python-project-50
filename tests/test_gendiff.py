from gendiff.diff import generate_diff
import pytest


def get_full_path(file_name):
        return f'./tests/fixtures/{file_name}'

@pytest.mark.parametrize('input1, input2, expected', [
    ('file1.json', 'file2.json', 'result.txt'),
    ('file1.yaml', 'file2.yaml', 'result.txt'),
    ('file1_tree.json', 'file2_tree.json', 'result_nested.txt'),
    ('file1_tree.yaml', 'file2_tree.yaml', 'result_nested.txt')
])

def test_generate_diff(input1, input2, expected):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2)
    with open(f'{get_full_path(expected)}') as correct:
        assert result == correct.read()
