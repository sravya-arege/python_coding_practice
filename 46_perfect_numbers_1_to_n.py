def perfect_numbers(limit):
    return [number for number in range(1, limit + 1) if is_perfect(number)]


def is_perfect(number):
    if number < 2:
        return False
    return sum(divisor for divisor in range(1, number) if number % divisor == 0) == number


limit = int(input("Enter n: "))
print("Perfect numbers:", perfect_numbers(limit))
