from hypothesis import given
from hypothesis import strategies as st

from fizzbuzz import fizzbuzz


def numbers_divisible_by_3_but_not_5():
    return st.integers(min_value=1, max_value=100).filter(
        lambda x: x % 3 == 0 and x % 5 != 0
    )


def numbers_divisible_by_5_but_not_3():
    return st.integers(min_value=1, max_value=100).filter(
        lambda x: x % 5 == 0 and x % 3 != 0
    )


def numbers_divisible_by_3_and_5():
    # Avoid HealthCheck.filter_too_much exception when using integers
    return st.sampled_from([15, 30, 45, 60, 75, 90])


def numbers_not_divisible_by_3_or_5():
    return st.integers(min_value=1, max_value=100).filter(
        lambda x: x % 5 != 0 and x % 3 != 0
    )


@given(num=numbers_divisible_by_3_but_not_5())
def test_number_divisible_by_3_but_not_5_returns_fizz(num: int):
    assert fizzbuzz(num) == "fizz"


@given(num=numbers_divisible_by_5_but_not_3())
def test_number_divisible_by_5_but_not_3_returns_buzz(num: int):
    assert fizzbuzz(num) == "buzz"


@given(num=numbers_divisible_by_3_and_5())
def test_number_divisible_by_3_and_5_returns_fizzbuzz(num: int):
    assert fizzbuzz(num) == "fizzbuzz"


@given(num=numbers_not_divisible_by_3_or_5())
def test_number_not_divisible_by_3_or_5_returns_number(num: int):
    assert fizzbuzz(num) == str(num)
