def count_even_odd(numbers):
    even = sum(number % 2 == 0 for number in numbers)
    return even, len(numbers) - even


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
even_count, odd_count = count_even_odd(numbers)
print("Even elements:", even_count)
print("Odd elements:", odd_count)
