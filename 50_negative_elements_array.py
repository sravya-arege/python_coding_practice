def negative_elements(numbers):
    return [number for number in numbers if number < 0]


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Negative elements:", negative_elements(numbers))
