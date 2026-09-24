def unique_elements(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Unique elements:", unique_elements(numbers))
