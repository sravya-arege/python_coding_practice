def second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
result = second_largest(numbers)
print("Second largest:", result if result is not None else "Not available")
