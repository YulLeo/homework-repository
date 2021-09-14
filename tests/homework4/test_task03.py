from homework4.task03 import my_precious_logger


def test_my_precious_logger_print_to_stderr_right(capsys):
    my_precious_logger('error: file not found')
    captured = capsys.readouterr()
    assert captured.err == 'error: file not found'


def test_my_precious_logger_print_to_stderr_not_to_stdout(capsys):
    my_precious_logger('error: file not found')
    captured = capsys.readouterr()
    assert captured.out != 'error: file not found'


def test_my_precious_logger_print_to_stdout_right(capsys):
    my_precious_logger('ok')
    captured = capsys.readouterr()
    assert captured.out == 'ok'
