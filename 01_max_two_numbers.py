def find_max(num1, num2):
    """Return the larger of two numbers."""
    if num1 > num2:
        return num1
    return num2


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = find_max(num1, num2)
print("Maximum:", result)
