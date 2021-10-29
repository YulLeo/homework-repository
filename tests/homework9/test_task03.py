import tempfile
from pathlib import Path

import pytest

from homework9.task03 import universal_file_counter

TEXT1 = 'line1 word word\nline2 word word word\nline3 word\nline4 word word\n'

TEXT2 = 'line1word word\nline2 word word word\nline3 word\nline word word wo\n'


@pytest.fixture()
def temp_directory():
    with tempfile.TemporaryDirectory() as directory:
        yield Path(str(directory))


def test_universal_file_counter_tokens(temp_directory):
    with open(temp_directory / 'file1.txt', 'w') as file:
        file.write(TEXT2)
    with open(temp_directory / 'file2.txt', 'w') as file:
        file.write(TEXT2)

    assert universal_file_counter(temp_directory, 'txt', str.split) == 24


def test_universal_file_counter_lines(temp_directory):
    with open(temp_directory / 'file1.txt', 'w') as file:
        file.write(TEXT1)
    with open(temp_directory / 'file2.txt', 'w') as file:
        file.write(TEXT2)

    assert universal_file_counter(temp_directory, 'txt') == 8


def test_universal_file_counter_tokens_dif_files(temp_directory):
    with open(temp_directory / 'file1.py', 'w') as file:
        file.write(TEXT1)
    with open(temp_directory / 'file2.txt', 'w') as file:
        file.write(TEXT2)

    assert universal_file_counter(temp_directory, 'txt', str.split) == 12


def test_universal_file_counter_lines_dif_files(temp_directory):
    with open(temp_directory / 'file1.py', 'w') as file:
        file.write(TEXT1)
    with open(temp_directory / 'file2.txt', 'w') as file:
        file.write(TEXT2)

    assert universal_file_counter(temp_directory, 'txt') == 4
