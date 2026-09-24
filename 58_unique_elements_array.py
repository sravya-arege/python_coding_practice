def unique_elements(numbers):
    return list(dict.fromkeys(numbers))


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Unique elements:", unique_elements(numbers))
