
def is_palindrome(number):
    """Return True if the number reads the same forward and backward."""
    if number < 0:
        return False

    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original == reversed_number


number = int(input("Enter a number: "))

if is_palindrome(number):
    print("Palindrome")
else:
    print("Not a Palindrome")
