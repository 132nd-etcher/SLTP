# coding=utf-8

import os
import time

import pytest

from sltp import SLTP
from .test_tables import test_tables


@pytest.fixture()
def remove_output():
    success = yield
    if success:
        try:
            os.remove('./output')
        except FileNotFoundError:
            pass


@pytest.mark.parametrize('test_table', test_tables)
def test_encode_decode(test_table):
    parser = SLTP()

    decoded_data = parser.decode(test_table)

    encoded_data = parser.encode(decoded_data)

    assert encoded_data == test_table
