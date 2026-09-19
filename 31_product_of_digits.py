def product_of_digits(number):
    """Return the product of all digits in an integer."""
    number = abs(number)

    if number == 0:
        return 0

    product = 1

    while number > 0:
        product *= number % 10
        number //= 10

    return product


number = int(input("Enter a number: "))
print("Product of digits:", product_of_digits(number))
