def print_table(number):
    """Print the multiplication table from 1 to 10."""
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")


number = int(input("Enter a number: "))
print_table(number)
