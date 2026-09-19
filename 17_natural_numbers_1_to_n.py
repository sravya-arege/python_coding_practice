def print_natural_numbers(n):
    """Print natural numbers from 1 to n."""
    number = 1
    while number <= n:
        print(number, end=" ")
        number += 1
    print()


n = int(input("Enter n: "))

if n < 1:
    print("Enter a positive integer.")
else:
    print_natural_numbers(n)
