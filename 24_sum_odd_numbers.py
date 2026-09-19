def sum_odd_numbers(n):
    """Return the sum of odd numbers from 1 to n."""
    total = 0
    number = 1

    while number <= n:
        total += number
        number += 2

    return total


n = int(input("Enter n: "))

if n < 1:
    print("Enter a positive integer.")
else:
    print("Sum of odd numbers:", sum_odd_numbers(n))
