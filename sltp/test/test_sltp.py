# coding=utf-8

import os

import pytest

from sltp import SLTP

TEST_FILES_DIR = './sltp/test/test_files'
ENCODING = 'iso8859_15'


@pytest.mark.parametrize('test_file', os.listdir(TEST_FILES_DIR))
def test_encode_decode_files(test_file):
    test_file = os.path.join(TEST_FILES_DIR, test_file)
    parser = SLTP()
    with open(test_file, encoding=ENCODING) as f:
        data = f.read()
    decoded_data = parser.decode(data)
    encoded_data = parser.encode(decoded_data)

    output = encoded_data.split('\n')
    input = data.split('\n')

    for x in input:
        assert x in output

    assert len(input) == len(output)
