import pytest
from exercises.basic import sum_of_digits, binary_string_to_int, count_numbers_and_letters, sum_of_cubes


#@pytest.mark.skip('Not yet implemented.')
def test_sum_of_digits():
    assert sum_of_digits(100) == 1
    assert sum_of_digits(22) == 4
    assert sum_of_digits(389) == 20
    assert sum_of_digits(300809) == 20
    assert sum_of_digits(9452388123) == 45


#@pytest.mark.skip('Not yet implemented.')
def test_binary_string_to_int():
    assert binary_string_to_int('101') == 5
    assert binary_string_to_int('1101') == 13
    assert binary_string_to_int('1000') == 8
    assert binary_string_to_int('11101001') == 233
    assert binary_string_to_int('10000101') == 133


#@pytest.mark.skip('Not yet implemented.')
def test_count_numbers_and_letters():
    count = count_numbers_and_letters('test 123')
    assert count['letters'] == 4
    assert count['numbers'] == 3

    count = count_numbers_and_letters('3l etters 2le tt ers')
    assert count['letters'] == 14
    assert count['numbers'] == 2

    count = count_numbers_and_letters('Svenska tecken (#) och VERSALER!')
    assert count['letters'] == 24
    assert count['numbers'] == 0


#@pytest.mark.skip('Not yet implemented.')
def test_sum_of_cubes():
    assert sum_of_cubes(4) == 100
    assert sum_of_cubes(1) == 1
    assert sum_of_cubes(10) == 3025
