import os

import pytest

from homework9.task01 import merge_sorted_files


@pytest.fixture()
def file_creator1():
    with open('temporary_file1', 'w'):
        pass
    yield 'temporary_file1'
    os.remove('temporary_file1')


@pytest.fixture()
def file_creator2():
    with open('temporary_file2', 'w'):
        pass
    yield 'temporary_file2'
    os.remove('temporary_file2')


def test_merge_sorted_files_equal_size(file_creator1, file_creator2):
    with open('temporary_file1', 'w') as file1, \
            open('temporary_file2', 'w') as file2:
        file1.write('5\n7\n8\n13\n')
        file2.write('1\n3\n9\n11\n')
    assert list(merge_sorted_files(
        ['temporary_file1', 'temporary_file2'])) == [1, 3, 5, 7, 8, 9, 11, 13]


def test_merge_sorted_files_unequal_size(file_creator1, file_creator2):
    with open('temporary_file1', 'w') as file1, \
            open('temporary_file2', 'w') as file2:
        file1.write('5\n7\n8\n13\n')
        file2.write('1\n3\n9\n')
    assert list(merge_sorted_files(
        ['temporary_file1', 'temporary_file2'])) == [1, 3, 5, 7, 8, 9, 13]


def test_merge_sorted_files_equal_nums(file_creator1, file_creator2):
    with open('temporary_file1', 'w') as file1, \
            open('temporary_file2', 'w') as file2:
        file1.write('1\n13\n')
        file2.write('1\n3\n9\n')
    assert list(merge_sorted_files(
        ['temporary_file1', 'temporary_file2'])) == [1, 1, 3, 9, 13]
