def is_prime(number):
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))


def split_numbers(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        numbers = [int(value) for value in file.read().split()]
    with open("even_numbers.txt", "w", encoding="utf-8") as even_file:
        even_file.write("\n".join(str(number) for number in numbers if number % 2 == 0))
    with open("odd_numbers.txt", "w", encoding="utf-8") as odd_file:
        odd_file.write("\n".join(str(number) for number in numbers if number % 2 != 0))
    with open("prime_numbers.txt", "w", encoding="utf-8") as prime_file:
        prime_file.write("\n".join(str(number) for number in numbers if is_prime(number)))


filename = input("Enter the input file name: ")
try:
    split_numbers(filename)
    print("Numbers written to separate files.")
except (FileNotFoundError, ValueError):
    print("The file was not found or contains invalid data.")
