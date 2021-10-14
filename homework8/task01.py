"""
We have a file that works as key-value storage, each line is represented
as key and value separated by = symbol,
example: name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be treated
both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys
and values accessible as collection items and as attributes.

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.

File size is expected to be small, you are permitted to read it
entirely into memory.
"""


class KeyValueStorage:
    """
    Wrapper class for the key value storage that works like
    its keys and values accessible as collection items and as
    attributes.
    """
    @staticmethod
    def clean_string(line: str) -> list:
        line = line.strip().split('=')
        for char in line:
            if char.isdigit():
                line[line.index(char)] = int(char)
        return line

    def __init__(self, path: str):
        self.path = path
        self.data = dict()
        with open(self.path) as file:
            for line in file:
                key, value = self.clean_string(line)
                if type(key) is int:
                    raise ValueError('Key cannot be an integer')
                self.data[key] = value

    def __getitem__(self, item: str) -> str:
        return self.data[item]

    def __getattr__(self, name: str) -> str:
        if hasattr(self, name):
            return getattr(self, name)

        return self.data[name]
