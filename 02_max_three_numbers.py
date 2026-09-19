def find_max(num1, num2, num3):
    """Return the largest of three numbers."""
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    return num3


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = find_max(num1, num2, num3)
print("Maximum:", result)
