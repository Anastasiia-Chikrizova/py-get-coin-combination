import pytest
from app import get_coin_combination


def test_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_one_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_one_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mixed_coins():
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(30) == [0, 0, 1, 1]


def test_large_amount():
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_boundary_conditions():
    assert get_coin_combination(4) == [4, 0, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]
