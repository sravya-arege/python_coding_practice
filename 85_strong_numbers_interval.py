def factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def is_strong(number):
    return number > 0 and sum(factorial(int(digit)) for digit in str(number)) == number


def strong_numbers_in_interval(start, end):
    return [number for number in range(start, end + 1) if is_strong(number)]


start = int(input("Enter interval start: "))
end = int(input("Enter interval end: "))
print("Strong numbers:", strong_numbers_in_interval(min(start, end), max(start, end)))
