def sum_first_last_digit(number):
    """Return the sum of the first and last digits."""
    number = abs(number)
    last_digit = number % 10

    while number >= 10:
        number //= 10

    first_digit = number
    return first_digit + last_digit


number = int(input("Enter a number: "))
print("Sum of first and last digit:", sum_first_last_digit(number))
