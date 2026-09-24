def armstrong_numbers(limit):
    return [number for number in range(1, limit + 1) if is_armstrong(number)]


def is_armstrong(number):
    digits = str(number)
    return sum(int(digit) ** len(digits) for digit in digits) == number


limit = int(input("Enter n: "))
print("Armstrong numbers:", armstrong_numbers(limit))
