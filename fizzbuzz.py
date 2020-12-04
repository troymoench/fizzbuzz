
def fizzbuzz(i: int) -> str:
    output = ""

    if i % 3 == 0:
        output += "fizz"
    if i % 5 == 0:
        output += "buzz"
    if not output:
        output = str(i)

    return output
