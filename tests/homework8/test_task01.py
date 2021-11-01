import os

import pytest

from homework8.task01 import KeyValueStorage


@pytest.fixture
def test_file():
    with open('temporary_file', 'w'):
        pass
    yield 'temporary_file'
    os.remove('temporary_file')


def test_key_value_storage_item_str(test_file):
    with open('temporary_file', 'w') as file:
        file.write('name=kek\nlast_name=top\n')
    storage = KeyValueStorage('temporary_file')
    assert storage['last_name'] == 'top'


def test_key_value_storage_item_int(test_file):
    with open('temporary_file', 'w') as file:
        file.write('name=kek\nlast_name=top\npower=9001\n')
    storage = KeyValueStorage('temporary_file')
    assert storage['power'] == 9001


def test_key_value_storage_attr_str(test_file):
    with open('temporary_file', 'w') as file:
        file.write('name=kek\nlast_name=top\n')
    storage = KeyValueStorage('temporary_file')
    assert storage.last_name == 'top'


def test_key_value_storage_attr_int(test_file):
    with open('temporary_file', 'w') as file:
        file.write('name=kek\nlast_name=top\npower=9001\n')
    storage = KeyValueStorage('temporary_file')
    assert storage.power == 9001


def test_key_value_storage_error_int(test_file):
    with pytest.raises(ValueError):
        with open('temporary_file', 'w') as file:
            file.write('name=kek\n2=top\npower=9001\n')
        KeyValueStorage('temporary_file')


def test_key_value_storage_attr_three_var(test_file):
    with open('temporary_file', 'w') as file:
        file.write('name=kek=45\nlast_name=top\npower=9001\n')
    storage = KeyValueStorage('temporary_file')
    assert storage.name == 'kek=45'
