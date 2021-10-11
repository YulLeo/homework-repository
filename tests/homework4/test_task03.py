from homework4.task03 import my_precious_logger

TEXT = 'ok'

ERROR_FILE_NOT_FOUND = 'error: file not found'


def test_my_precious_logger_print_to_stderr_right(capsys):
    my_precious_logger(ERROR_FILE_NOT_FOUND)
    captured = capsys.readouterr()
    assert captured.err == ERROR_FILE_NOT_FOUND


def test_my_precious_logger_print_to_stderr_not_to_stdout(capsys):
    my_precious_logger(ERROR_FILE_NOT_FOUND)
    captured = capsys.readouterr()
    assert captured.out != ERROR_FILE_NOT_FOUND


def test_my_precious_logger_print_to_stdout_right(capsys):
    my_precious_logger(TEXT)
    captured = capsys.readouterr()
    assert captured.out == TEXT
