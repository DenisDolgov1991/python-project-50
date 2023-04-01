from gendiff.diff import generate_diff


def test_gendiff():
    file1_path = '.tests/fixtures/file1.json'
    file2_path = '.tests/fixtures/file2.json'
    result = generate_diff(file1_path, file2_path)
    output = open('.tests/fixtures/ouput_json.txt')

    assert result == output
