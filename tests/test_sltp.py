# coding=utf-8

from sltp import SLTP


def test_sltp():
    parser = SLTP()
    with open('./tests/test_table') as f:
        decoded_data = parser.decode(f.read())
