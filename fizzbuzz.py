
def fizzbuzz(i: int) -> str:
    if i % 3 == 0 and i % 5 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return str(i)
