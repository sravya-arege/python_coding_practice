def is_perfect(number):
    return number > 1 and sum(divisor for divisor in range(1, number) if number % divisor == 0) == number


def perfect_numbers_in_interval(start, end):
    return [number for number in range(start, end + 1) if is_perfect(number)]


start = int(input("Enter interval start: "))
end = int(input("Enter interval end: "))
print("Perfect numbers:", perfect_numbers_in_interval(min(start, end), max(start, end)))
