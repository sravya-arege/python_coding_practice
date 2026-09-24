def factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def is_strong(number):
    return sum(factorial(int(digit)) for digit in str(number)) == number


def strong_numbers(limit):
    return [number for number in range(1, limit + 1) if is_strong(number)]


limit = int(input("Enter n: "))
print("Strong numbers:", strong_numbers(limit))
