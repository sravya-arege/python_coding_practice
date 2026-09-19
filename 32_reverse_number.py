def reverse_number(number):
    """Return the reversed integer."""
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_number = 0

    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10

    return sign * reversed_number


number = int(input("Enter a number: "))
print("Reversed number:", reverse_number(number))
