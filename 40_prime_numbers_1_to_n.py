def primes_up_to(limit):
    primes = []
    for number in range(2, limit + 1):
        if all(number % divisor for divisor in range(2, int(number ** 0.5) + 1)):
            primes.append(number)
    return primes


limit = int(input("Enter n: "))
print("Prime numbers:", primes_up_to(limit))
