import urllib
from unittest import mock

import pytest

from homework4.task02 import count_dots_on_i


@mock.patch('homework4.task02.request.urlopen', return_value=[b'iii'])
def test_count_dots_on_i_positive_with_i(mock_patch):
    assert count_dots_on_i('https://example.com/') == 3


@mock.patch('homework4.task02.request.urlopen', return_value=[b'abgfuyn'])
def test_count_dots_on_i_positive_without_i(mock_patch):
    assert count_dots_on_i('https://example.com/') == 0


@mock.patch(
    'homework4.task02.request.urlopen',
    side_effect=urllib.error.URLError('')
)
def test_count_dots_on_i_negative_raise_error(mock_patch):
    with pytest.raises(ValueError):
        count_dots_on_i('https://example.com/')
