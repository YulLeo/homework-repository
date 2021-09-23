from typing import List

from homework2.constant import ENCODING
from homework2.task01_utils import (count_common_non_ascii_char,
                                    find_rare_char, get_char_sequence,
                                    get_words_with_unique_symbols,
                                    non_ascii_chars, punctuation_counter,
                                    unique_words)


def get_longest_diverse_words(file_path: str, encoding=ENCODING) -> List[str]:
    """
    Takes text file and returns 10 longest words consisting from largest amount
    of unique symbols.
    """
    with open(file_path, encoding=encoding) as file:
        words = unique_words(file)
        return get_words_with_unique_symbols(words)


def get_rarest_char(file_path: str, encoding=ENCODING) -> str:
    """Finds rarest symbol for document"""
    with open(file_path, encoding=encoding) as file:
        char_seq = get_char_sequence(file)
        return find_rare_char(char_seq)


def count_punctuation_chars(file_path: str, encoding=ENCODING) -> int:
    """Counts every punctuation char for document"""
    with open(file_path, encoding=encoding) as file:
        char_sequence = get_char_sequence(file)
        return punctuation_counter(char_sequence)


def count_non_ascii_chars(file_path: str, encoding=ENCODING) -> int:
    """Counts every non ascii char for document"""
    with open(file_path, encoding=encoding) as file:
        char_sequence = get_char_sequence(file)
        return non_ascii_chars(char_sequence)


def get_most_common_non_ascii_char(file_path: str, encoding=ENCODING) -> str:
    """finds the most common non ascii char for document"""
    with open(file_path, encoding=encoding) as file:
        char_sequence = get_char_sequence(file)
        return count_common_non_ascii_char(char_sequence)
