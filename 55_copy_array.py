def copy_array(numbers):
    return numbers.copy()


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Copied array:", copy_array(numbers))
