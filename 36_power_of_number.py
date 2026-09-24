def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


base = int(input("Enter the base: "))
exponent = int(input("Enter a non-negative exponent: "))
print("Power:", calculate_power(base, exponent))
