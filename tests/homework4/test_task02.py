import urllib
from unittest import mock

import pytest

from homework4.task02 import count_chars

REQUEST_URLOPEN = 'homework4.task02.request.urlopen'

SYMBOL = b'i'

URL = 'https://example.com/'


@mock.patch(REQUEST_URLOPEN, return_value=[b'iii'])
def test_count_dots_on_i_positive_with_i(mock_patch):
    assert count_chars(URL, SYMBOL) == 3


@mock.patch(REQUEST_URLOPEN, return_value=[b'abgfuyn'])
def test_count_dots_on_i_positive_without_i(mock_patch):
    assert count_chars(URL, SYMBOL) == 0


@mock.patch(REQUEST_URLOPEN, side_effect=urllib.error.URLError(''))
def test_count_dots_on_i_negative_raise_error(mock_patch):
    with pytest.raises(ValueError):
        count_chars(URL, SYMBOL)
