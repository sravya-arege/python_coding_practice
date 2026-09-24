def is_prime(number):
    return number >= 2 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))


def primes_in_interval(start, end):
    return [number for number in range(start, end + 1) if is_prime(number)]


start = int(input("Enter interval start: "))
end = int(input("Enter interval end: "))
print("Prime numbers:", primes_in_interval(min(start, end), max(start, end)))
