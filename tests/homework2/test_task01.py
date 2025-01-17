from homework2.task01_utils import (count_common_non_ascii_char,
                                    find_rare_char,
                                    get_words_with_unique_symbols,
                                    non_ascii_chars, punctuation_counter)


def test_count_common_non_ascii_char_right():
    assert count_common_non_ascii_char((
        'ä', 'ä', 'ö', 'ä', 'ö', 'a', 'g', 'h')) == 'ä'


def test_count_common_non_ascii_char_wrong():
    assert count_common_non_ascii_char((
        'ä', 'ä', 'ö', 'ä', 'ö', 'a', 'g', 'h')) != 'ö'


def test_non_ascii_chars_right():
    assert non_ascii_chars(('ä', 'ä', 'ä', 'ä', 'ä', 'a', 'g', 'h')) == 5


def test_non_ascii_chars_wrong():
    assert non_ascii_chars(('ä', 'ä', 'ä', 'ä', 'ä', 'a', 'g', 'h')) != 6


def test_punctuation_counter_right():
    assert punctuation_counter(('y', 'b', 'k', ',', ':')) == 2


def test_punctuation_counter_wrong():
    assert punctuation_counter(('y', 'b', 'k', ',', ':')) != 1


def test_find_rare_char_right():
    assert find_rare_char(('a', 'a', 'v', 'b', 'u', 'u', 'u', 'b')) == 'v'


def test_find_rare_char_wrong():
    assert find_rare_char(('a', 'a', 'v', 'b', 'u', 'u', 'u', 'b')) != 'a'


def test_get_words_with_unique_symbols_wrong():
    assert get_words_with_unique_symbols(
        {
            'abenteuerliche',
            'zeitmauer',
            'ssssssssddddfdfdfd',
            'hertz',
            'schutzumschlag',
            'opus',
            'defghybcr',
            'fd',
            'spiegelbild',
            'achtzehnten',
            'starken'
        }
    ) != [
        'spiegelbild',
        'defghybcr',
        'abenteuerliche',
        'schutzumschlag',
        'zeitmauer',
        'achtzehnten',
        'starken',
        'hertz',
        'opus',
        'ssssssssddddfdfdfd'
          ]


def test_get_words_with_unique_symbols_right():
    assert get_words_with_unique_symbols(
        {
            'abc',
            'abcd',
            'ssssssssabcdu',
            'abcdefy',
            'bcdefgyt',
            'sdfghjklllliu',
            'fd',
            'zxcvbnmasdf',
            'qqqqwwasdfghj',
            's'
        }
    ) == [
        'zxcvbnmasdf',
        'sdfghjklllliu',
        'qqqqwwasdfghj',
        'bcdefgyt',
        'abcdefy',
        'ssssssssabcdu',
        'abcd',
        'abc',
        'fd',
        's'
    ]
