
def main():
    x = 4
    price = 99.99

    discount = 0.12

    result = price * ( 1 - discount )

    print(result)

    name = "Rolf"

    name = "Bob"

    a = 25

    b = a

    print(a)
    print(b)

    var1 = 215
    var2 = 215

    num1 = 2
    num2 = 8

    # string formatting, f-strings available in Python 3.6 onwards.

    name = "Bob"
    greeting = f"Hello, {name}"

    print(greeting)

    name = "Rolf"
    greeting = "Hello, {}"
    with_name = greeting.format(name)

    print(with_name)

    longer_phrase = "Hello, {}. Today is {}."

    formatted = longer_phrase.format("Rolf", "Monday")
    print(formatted)


if __name__ == "__main__":
    main()