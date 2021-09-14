import os

import pytest

from homework4.task01 import read_magic_number


@pytest.fixture()
def file_creator():
    with open('temporary_file', 'w'):
        pass
    yield 'temporary_file'
    os.remove('temporary_file')


def test_read_magic_number_exists_true(file_creator):
    with open(file_creator, 'w') as file:
        file.write('2')
    assert read_magic_number(file_creator) is True


def test_read_magic_number_exists_false(file_creator):
    with open(file_creator, 'w') as file:
        file.write('4')
    assert read_magic_number(file_creator) is False


def test_read_magic_number_exists_not_num(file_creator):
    with open(file_creator, 'w') as file:
        file.write('oi')
    assert read_magic_number(file_creator) is False


def test_read_magic_number_exists_empty(file_creator):
    assert read_magic_number(file_creator) is False


def test_read_magic_number_not_exists():
    assert read_magic_number('abcc') == 'File Not Found'
