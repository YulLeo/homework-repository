import string
import textwrap
import unicodedata
from collections import Counter
from typing import List, Sequence


def get_word_sequence(file) -> List[str]:
    """ Returns word sequence for a document"""
    for doc_line in file:
        doc_line = textwrap.wrap(doc_line)
        for wrapped_line in doc_line:
            split_line = wrapped_line.split()
            for word in split_line:
                yield word.lower()


def get_char_sequence(file) -> List[str]:
    """ Returns char sequence for a document"""
    for line in file:
        for char in line:
            yield char.lower()


def unique_words(file) -> set[str]:
    """ Takes text file and returns set with unique words."""
    words = set()
    expand_punctuation = expand_string_punctuation(file)
    file.seek(0)
    word_sequence = get_word_sequence(file)
    for word in word_sequence:
        word = word.strip(expand_punctuation)
        words.add(word)
    return words


def get_words_with_unique_symbols(words: set[str]) -> List[str]:
    """
    Takes set with unique words and returns 10 longest words
    consisting from largest amount of unique symbols.
    """
    chars = {}
    for word in words:
        unique_char_in_word = ''.join(set(word))
        chars[word] = len(unique_char_in_word)
    sorted_chars = sorted(
        chars.items(), key=lambda item: item[1], reverse=True)
    return [char[0] for char in sorted_chars[:10]]


def expand_string_punctuation(file_path: str) -> str:
    """
    Enriches standard punctuation collection by non-standard
    symbols from file
    """
    char_seq = get_char_sequence(file_path)
    string_punctuation_expanded = string.punctuation
    text_punctuation = {i for i in char_seq if is_punct(i)}
    for char in text_punctuation:
        if char not in string.punctuation:
            string_punctuation_expanded += char
    return string_punctuation_expanded


def find_rare_char(char_seq: Sequence[str]) -> str:
    """Finds rarest symbol for sequence"""
    data = Counter(char_seq)
    return str(data.most_common()[-1][0])


def punctuation_counter(char_sequence: Sequence[str]) -> int:
    """Counts every punctuation char for sequence"""
    return len([char for char in char_sequence if is_punct(char)])


def is_punct(char):
    return unicodedata.category(char).startswith('P')


def non_ascii_chars(char_sequence: Sequence[str]) -> int:
    """counts every non ascii char for sequence"""
    non_ascii_ch = [char for char in char_sequence if char.isascii() is False]
    return len(non_ascii_ch)


def count_common_non_ascii_char(char_sequence: Sequence[str]) -> str:
    """finds the most common non ascii char for sequence"""
    non_ascii_char = [
        char for char in char_sequence if char.isascii() is False]
    char_counter = Counter(non_ascii_char)
    return char_counter.most_common(1)[0][0]
