import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)


from gendiff.generate_diff import generate_diff
import pytest

def test_generate_diff():
    file1 = json.load(open('tests/fixtures/file_1.json'))
    file2 = json.load(open('tests/fixtures/file_2.json'))
    result = '''{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}'''

    assert generate_diff(file1, file2) == result
