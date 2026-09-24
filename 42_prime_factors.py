def prime_factors(number):
    factors = []
    divisor = 2
    number = abs(number)
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.append(number)
    return factors


number = int(input("Enter a number: "))
if abs(number) < 2:
    print("No prime factors")
else:
    print("Prime factors:", prime_factors(number))
