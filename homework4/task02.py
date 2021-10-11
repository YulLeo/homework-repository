"""
task_2_mock_input:

Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
"""

import urllib.error
from urllib import request


def count_chars(url: str, symbol: bytes) -> int:
    """
    Accepts an URL as input and count how many times
    a particular symbol is in the HTML by this URL.
    """
    try:
        return sum(char.count(symbol) for char in request.urlopen(url))
    except urllib.error.URLError:
        raise ValueError(f'Unreachable {url}')
