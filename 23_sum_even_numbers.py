def sum_even_numbers(n):
    """Return the sum of even numbers from 1 to n."""
    total = 0
    number = 2

    while number <= n:
        total += number
        number += 2

    return total


n = int(input("Enter n: "))

if n < 1:
    print("Enter a positive integer.")
else:
    print("Sum of even numbers:", sum_even_numbers(n))
