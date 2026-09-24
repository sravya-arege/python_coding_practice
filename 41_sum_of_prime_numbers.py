def sum_of_primes(limit):
    total = 0
    for number in range(2, limit + 1):
        if all(number % divisor for divisor in range(2, int(number ** 0.5) + 1)):
            total += number
    return total


limit = int(input("Enter n: "))
print("Sum of prime numbers:", sum_of_primes(limit))
