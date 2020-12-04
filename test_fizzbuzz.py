from fizzbuzz import fizzbuzz

def test_number_divisible_by_3_but_not_5_returns_fizz():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(6) == "fizz"
    assert fizzbuzz(18) == "fizz"

def test_number_divisible_by_5_but_not_3_returns_buzz():
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(10) == "buzz"
    assert fizzbuzz(20) == "buzz"

def test_number_divisible_by_3_and_5_returns_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(30) == "fizzbuzz"

def test_number_not_divisible_by_3_or_5_returns_number():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"
