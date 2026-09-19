def count_digits(number):
    """Return the number of digits in an integer."""
    number = abs(number)

    if number == 0:
        return 1

    count = 0
    while number > 0:
        number //= 10
        count += 1

    return count


number = int(input("Enter a number: "))
print("Number of digits:", count_digits(number))
