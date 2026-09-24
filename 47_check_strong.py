def factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def is_strong(number):
    return number >= 0 and sum(factorial(int(digit)) for digit in str(number)) == number


number = int(input("Enter a number: "))
print("Strong" if is_strong(number) else "Not strong")
