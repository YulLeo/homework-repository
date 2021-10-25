"""
Write a function that takes directory path,
a file extension and an optional tokenizer.
It will count lines in all files with that extension
if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""

from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(dir_path: Path,
                           file_extension: str,
                           tokenizer: Optional[Callable] = None) -> int:
    """
    count lines in all files with that extension if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens.
    """
    files = (
        file for file in dir_path.iterdir()
        if file.suffix == f'.{file_extension}'
    )
    return sum(
        get_number_of_all_tokens(file_path, tokenizer)
        for file_path in files
    )


def get_number_of_all_tokens(file_path, tokenizer):
    """
    Counts the number of tokens in particular file.
    If tokenizer is None returns number of lines.
    """
    with open(file_path) as file:
        return sum(get_number_of_token(line, tokenizer) for line in file)


def get_number_of_token(line, tokenizer):
    """
    Counts the number of tokens in line.
    If tokenizer is None returns 1.
    """
    return sum(1 for token in tokenizer(line)) if tokenizer is not None else 1
