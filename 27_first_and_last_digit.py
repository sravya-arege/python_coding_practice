def first_and_last_digit(number):
    """Return the first and last digits of an integer."""
    number = abs(number)
    last_digit = number % 10

    while number >= 10:
        number //= 10

    first_digit = number
    return first_digit, last_digit


number = int(input("Enter a number: "))
first_digit, last_digit = first_and_last_digit(number)

print("First digit:", first_digit)
print("Last digit:", last_digit)
