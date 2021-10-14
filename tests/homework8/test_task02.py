import sqlite3
from contextlib import contextmanager
from pathlib import Path

from homework8.task02 import TableData

TABLE_NAME = 'presidents'
DATABASE_NAME = Path(__file__).parent / 'example.sqlite'

DELETE = 'DELETE FROM presidents WHERE name = ?'
INSERT = 'INSERT INTO presidents (name, age, country) VALUES (?, ?, ?)'


@contextmanager
def putin():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(INSERT, ('Putin', 235, 'Russia'))
        conn.commit()
        yield
    finally:
        cursor.execute(DELETE, ('Putin',))
        conn.commit()
        conn.close()


def test_table_data_len():
    presidents = TableData(database_name=DATABASE_NAME, table_name=TABLE_NAME)
    assert len(presidents) == 3


def test_table_data_contains():
    presidents = TableData(database_name=DATABASE_NAME, table_name=TABLE_NAME)
    assert 'Yeltsin' in presidents


def test_table_data_not_contains():
    presidents = TableData(database_name=DATABASE_NAME, table_name=TABLE_NAME)
    assert 'Putin' not in presidents


def test_table_data_iterable():
    presidents = TableData(database_name=DATABASE_NAME, table_name=TABLE_NAME)
    surnames = [president[0] for president in presidents]
    assert surnames == ['Yeltsin', 'Trump', 'Big Man Tyrone']


def test_table_data_getitem():
    presidents = TableData(database_name=DATABASE_NAME, table_name=TABLE_NAME)
    assert presidents['Trump'] == ('Trump', 1337, 'US')


def test_table_actual_data():
    presidents = TableData(database_name=DATABASE_NAME, table_name=TABLE_NAME)
    assert 'Putin' not in presidents
    assert len(presidents) == 3

    with putin():
        assert 'Putin' in presidents
        assert len(presidents) == 4

    assert 'Putin' not in presidents
    assert len(presidents) == 3
