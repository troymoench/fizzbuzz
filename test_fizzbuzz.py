from fizzbuzz import fizzbuzz

def test_number_divisible_by_3_returns_fizz():
    assert fizzbuzz(3) == "fizz"

def test_number_divisible_by_5_returns_buzz():
    assert fizzbuzz(5) == "buzz"

def test_number_divisible_by_3_and_5_returns_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"

def test_number_not_divisible_by_3_or_5_returns_number():
    assert fizzbuzz(1) == "1"
