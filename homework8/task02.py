"""
Write a wrapper class TableData for database table, that when initialized
with database name and table acts as collection object (implements
Collection protocol). Assume all data has unique values in 'name' column.

Avoid reading entire table into memory. When iterating through records,
start reading the first record,
then go to the next one, until records are exhausted. When writing tests,
it's not always necessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""

import sqlite3
from contextlib import contextmanager
from typing import Generator


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    @contextmanager
    def _table_safe_connection(self, conn=None) -> sqlite3.Cursor:
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            yield cursor
        finally:
            if conn is not None:
                conn.close()

    def __getitem__(self, item):
        with self._table_safe_connection() as cursor:
            for items in cursor.execute(
                    f'SELECT * FROM {self.table_name}'
            ).fetchall():
                if item in items:
                    return items

    def __len__(self) -> int:
        with self._table_safe_connection() as cursor:
            return cursor.execute(
                f'SELECT COUNT(*) FROM {self.table_name}'
            ).fetchone()[0]

    def __contains__(self, item) -> bool:
        with self._table_safe_connection() as cursor:
            for items in cursor.execute(
                    f'SELECT * FROM {self.table_name}'
            ).fetchall():
                if item in items:
                    return True

            return False

    def __iter__(self) -> Generator:
        with self._table_safe_connection() as cursor:
            yield from cursor.execute(
                    f'SELECT * FROM {self.table_name}'
            ).fetchall()
