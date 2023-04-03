from gendiff.diff import generate_diff
import pytest
from tests import get_full_path


@pytest.mark.parametrize('input1, input2', [
    ('result.txt', 'result_tree.txt'),
])
def test_exception_in_generate_diff(input1, input2):
    file1, file2 = map(get_full_path, (input1, input2))
    with pytest.raises(Exception) as e:
        generate_diff(file1, file2)
    assert str(e.value) == \
        'Comparison is available only for json and yaml files'
