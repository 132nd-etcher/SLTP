# coding=utf-8

import os

import pytest

from sltp import SLTP


@pytest.fixture()
def remove_output():
    yield
    os.remove('./output')


# noinspection PyUnusedLocal, PyShadowingNames
def test_sltp(remove_output):
    parser = SLTP()

    with open('./sltp/tests/test_table', encoding='iso8859_15') as f:
        decoded_data = parser.decode('\n'.join(f.readlines()[1:]))

    encoded_data = parser.encode(decoded_data)

    with open('./output', encoding='iso8859_15', mode='w') as f:
        f.write('mission =' + encoded_data + '\n')

    with open('./output', encoding='iso8859_15') as out, open('./sltp/tests/test_table', encoding='iso8859_15') as in_:
        assert in_.readlines() == out.readlines()
