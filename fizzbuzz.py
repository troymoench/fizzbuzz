
def fizzbuzz(i: int) -> str:
    if i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    elif i % 3 == 0 and i % 5 == 0:
        return "fizzbuzz"
    else:
        return str(i)
