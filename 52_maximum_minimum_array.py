def maximum_and_minimum(numbers):
    return max(numbers), min(numbers)


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
if numbers:
    maximum, minimum = maximum_and_minimum(numbers)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
else:
    print("The array is empty.")
