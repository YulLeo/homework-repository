"""
task_3_get_print_output:

Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests
You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""

import sys


def my_precious_logger(text: str):
    """
    Receive a string and write it to stderr
    if line starts with "error" and to the stdout otherwise.
    """
    first_letters = text[0:5]
    if first_letters == 'error':
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)
