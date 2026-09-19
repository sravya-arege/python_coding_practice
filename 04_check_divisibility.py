def check_divisible(number):
    """Check whether a number is divisible by both 5 and 11."""
    if number % 5 == 0 and number % 11 == 0:
        return "Divisible by 5 and 11"
    return "Not divisible by 5 and 11"


number = int(input("Enter a number: "))
print(check_divisible(number))
