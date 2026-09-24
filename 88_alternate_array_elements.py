def alternate_elements(numbers):
    return numbers[::2]


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Alternate elements:", alternate_elements(numbers))
