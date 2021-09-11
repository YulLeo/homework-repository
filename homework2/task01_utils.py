import string
import textwrap
import unicodedata
from collections import Counter
from typing import Any, Generator, List, TextIO


def get_word_sequence(file: TextIO) -> Generator[Any, Any, None]:
    """ Returns word sequence for a document"""
    noble_line_list = (
        textwrap.wrap(line)[0] for line in file if len(textwrap.wrap(line)
                                                       ) > 0)
    for line in noble_line_list:
        yield from line.lower().split()


def get_char_sequence(file: TextIO) -> Generator[Any, Any, None]:
    """ Returns char sequence for a document"""
    line = (line for line in file)
    for char in line:
        yield from char


def unique_words(file: TextIO) -> set[str]:
    """ Takes text file and returns set with unique words."""
    expand_punctuation = expand_string_punctuation(file)
    file.seek(0)
    words = set(
        word.strip(expand_punctuation) for word in get_word_sequence(file))
    return words


def get_words_with_unique_symbols(words: set[str]) -> List[str]:
    """
    Takes set with unique words and returns 10 longest words
    consisting from largest amount of unique symbols.
    """
    word_list = [(word, len(set(word))) for word in words]
    sorted_word_list = sorted(
        word_list, key=lambda item: item[1], reverse=True)
    return [word[0] for word in sorted_word_list[:10]]


def expand_string_punctuation(file: TextIO) -> str:
    """
    Enriches standard punctuation collection by non-standard
    symbols from file
    """
    char_seq = get_char_sequence(file)
    return string.punctuation + "".join(
        {i for i in char_seq if is_punct(i) and i not in string.punctuation}
    )


def find_rare_char(char_seq: Generator[Any, Any, None]) -> str:
    """Finds rarest symbol for sequence"""
    data = Counter(char_seq)
    return str(data.most_common()[-1][0])


def punctuation_counter(char_sequence: Generator[Any, Any, None]) -> int:
    """Counts every punctuation char for sequence"""
    return len([char for char in char_sequence if is_punct(char)])


def is_punct(char: str) -> bool:
    """Verify that char belongs to punctuation unicode data category"""
    return unicodedata.category(char).startswith('P')


def non_ascii_chars(char_sequence: Generator[Any, Any, None]) -> int:
    """Counts every non ascii char for sequence"""
    non_ascii_ch = [char for char in char_sequence if char.isascii() is False]
    return len(non_ascii_ch)


def count_common_non_ascii_char(
        char_sequence: Generator[Any, Any, None]) -> str:
    """finds the most common non ascii char for sequence"""
    non_ascii_char = [
        char for char in char_sequence if char.isascii() is False]
    char_counter = Counter(non_ascii_char)
    return char_counter.most_common(1)[0][0]
