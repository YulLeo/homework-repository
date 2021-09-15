from homework4.task05 import fizzbuzz


def test_fizzbuzz_fizzbuzz_num():
    assert list(fizzbuzz(15))[14] == 'FizzBuzz'


def test_fizzbuzz_fizz_num():
    assert list(fizzbuzz(15))[11] == 'Fizz'


def test_fizzbuzz_buzz_num():
    assert list(fizzbuzz(15))[9] == 'Buzz'


def test_fizzbuzz_num():
    assert list(fizzbuzz(15))[1] == '2'
