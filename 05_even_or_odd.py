def check_even_odd(number):
    """Return whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"


number = int(input("Enter a number: "))
result = check_even_odd(number)

print("The number is:", result)
