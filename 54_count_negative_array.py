def count_negative(numbers):
    return sum(number < 0 for number in numbers)


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Negative element count:", count_negative(numbers))
