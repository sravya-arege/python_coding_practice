def check_number(number):
    """Return whether a number is positive, negative, or zero."""
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"


number = int(input("Enter a number: "))
result = check_number(number)

print("The number is:", result)
