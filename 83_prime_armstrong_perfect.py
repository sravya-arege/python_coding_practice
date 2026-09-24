def is_prime(number):
    return number >= 2 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))


def is_armstrong(number):
    digits = str(number)
    return number >= 0 and sum(int(digit) ** len(digits) for digit in digits) == number


def is_perfect(number):
    return number > 1 and sum(divisor for divisor in range(1, number) if number % divisor == 0) == number


number = int(input("Enter a number: "))
print("Prime:", is_prime(number))
print("Armstrong:", is_armstrong(number))
print("Perfect:", is_perfect(number))
