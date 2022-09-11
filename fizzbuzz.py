def fizzbuzz(i: int) -> str:
    output = ""

    if i % 3 == 0:
        output += "fizz"
    if i % 5 == 0:
        output += "buzz"
    if not output:
        output = str(i)

    return output


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
