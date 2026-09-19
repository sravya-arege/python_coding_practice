def print_reverse_numbers(n):
    """Print natural numbers in reverse order."""
    while n >= 1:
        print(n, end=" ")
        n -= 1
    print()


n = int(input("Enter n: "))

if n < 1:
    print("Enter a positive integer.")
else:
    print_reverse_numbers(n)
