def is_armstrong(number):
    digits = str(number)
    return number >= 0 and sum(int(digit) ** len(digits) for digit in digits) == number


def armstrong_numbers_in_interval(start, end):
    return [number for number in range(start, end + 1) if is_armstrong(number)]


start = int(input("Enter interval start: "))
end = int(input("Enter interval end: "))
print("Armstrong numbers:", armstrong_numbers_in_interval(min(start, end), max(start, end)))
