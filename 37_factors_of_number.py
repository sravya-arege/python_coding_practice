def find_factors(number):
    factors = []
    for value in range(1, abs(number) + 1):
        if number % value == 0:
            factors.append(value)
    return factors


number = int(input("Enter a number: "))
if number == 0:
    print("Every non-zero number is a factor of 0.")
else:
    print("Factors:", find_factors(number))
