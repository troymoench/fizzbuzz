from hypothesis import given
from hypothesis import strategies as st

from fizzbuzz import fizzbuzz


def numbers_divisible_by_3_but_not_5():
    return st.integers(min_value=0).filter(lambda x: x % 3 == 0 and x % 5 != 0)


def numbers_divisible_by_5_but_not_3():
    return st.just(5) | st.just(10) | st.just(20)


def numbers_divisible_by_3_and_5():
    return st.just(15) | st.just(30)


def numbers_not_divisible_by_3_or_5():
    return st.just(1) | st.just(2) | st.just(4)


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
