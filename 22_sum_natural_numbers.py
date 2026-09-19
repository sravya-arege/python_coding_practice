def sum_natural_numbers(n):
    """Return the sum of natural numbers from 1 to n."""
    total = 0
    number = 1

    while number <= n:
        total += number
        number += 1

    return total


n = int(input("Enter n: "))

if n < 1:
    print("Enter a positive integer.")
else:
    print("Sum:", sum_natural_numbers(n))
