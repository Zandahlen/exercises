import pytest
from exercises.advanced import factorial, yahtzee_score


#@pytest.mark.skip('Not yet implemented.')
def test_factorial():
    assert sorted(factorial(1)) == [1]
    assert sorted(factorial(2)) == [2]
    assert sorted(factorial(7)) == [7]
    assert sorted(factorial(21)) == [3, 7]
    assert sorted(factorial(40)) == [2, 2, 2, 5]
    assert sorted(factorial(693)) == [3, 3, 7, 11]
    assert sorted(factorial(39270)) == [2, 3, 5, 7, 11, 17]


#@pytest.mark.skip('Not yet implemented.')
def test_yahtzee_score():
    assert yahtzee_score([5, 5, 5, 5, 5], 'yahtzee') == 50
    assert yahtzee_score([5, 5, 5, 5, 4], 'yahtzee') == False
    assert yahtzee_score([2, 5, 6, 3, 1], 'chance') == 17

    assert yahtzee_score([6, 2, 3, 4, 5], 'large_straight') == 40
    assert yahtzee_score([6, 1, 3, 4, 5], 'large_straight') == False

    assert yahtzee_score([1, 2, 3, 4, 5], 'small_straight') == 30
    assert yahtzee_score([1, 2, 3, 4, 2], 'small_straight') == False

    assert yahtzee_score([2, 1, 3, 4, 1], 'aces') == 2
    assert yahtzee_score([2, 2, 3, 6, 1], 'twos') == 4
    assert yahtzee_score([2, 1, 3, 4, 1], 'threes') == 3
    assert yahtzee_score([2, 4, 3, 4, 1], 'fours') == 8
    assert yahtzee_score([2, 5, 5, 4, 5], 'fives') == 15
    assert yahtzee_score([6, 6, 6, 4, 6], 'sixes') == 24

    assert yahtzee_score([2, 6, 3, 4, 3], 'aces') == False
    assert yahtzee_score([1, 4, 3, 6, 1], 'twos') == False
    assert yahtzee_score([2, 1, 6, 4, 1], 'threes') == False
    assert yahtzee_score([2, 2, 3, 1, 1], 'fours') == False
    assert yahtzee_score([2, 6, 6, 4, 3], 'fives') == False
    assert yahtzee_score([2, 2, 5, 4, 1], 'sixes') == False

    assert yahtzee_score([1, 5, 6, 6, 6], 'three_of_a_kind') == 18
    assert yahtzee_score([3, 5, 5, 5, 1], 'three_of_a_kind') == 15
    assert yahtzee_score([6, 4, 4, 5, 4], 'three_of_a_kind') == 12
    assert yahtzee_score([3, 5, 3, 3, 1], 'three_of_a_kind') == 9
    assert yahtzee_score([2, 5, 2, 6, 2], 'three_of_a_kind') == 6
    assert yahtzee_score([6, 1, 1, 6, 1], 'three_of_a_kind') == 3
    assert yahtzee_score([6, 5, 6, 6, 1], 'three_of_a_kind') == 18

    assert yahtzee_score([1, 6, 6, 6, 6], 'four_of_a_kind') == 24
    assert yahtzee_score([1, 5, 5, 5, 5], 'four_of_a_kind') == 20
    assert yahtzee_score([4, 4, 2, 4, 4], 'four_of_a_kind') == 16
    assert yahtzee_score([3, 3, 3, 5, 3], 'four_of_a_kind') == 12
    assert yahtzee_score([2, 6, 2, 2, 2], 'four_of_a_kind') == 8
    assert yahtzee_score([1, 1, 4, 1, 1], 'four_of_a_kind') == 4
    assert yahtzee_score([1, 1, 1, 1, 1], 'four_of_a_kind') == 4
    assert yahtzee_score([6, 6, 6, 6, 6], 'four_of_a_kind') == 24

    assert yahtzee_score([6, 6, 5, 5, 5], 'full_house') == 25
    assert yahtzee_score([5, 1, 5, 1, 5], 'full_house') == 25
    assert yahtzee_score([4, 4, 4, 2, 4], 'full_house') == False

@pytest.mark.skip('Not yet implemented.')
def test_blackjack_score():
    pass  # Här skriver du som elev tester till uppgiften.
