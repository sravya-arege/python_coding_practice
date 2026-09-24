def duplicate_count(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return sum(1 for count in counts.values() if count > 1)


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Number of duplicate values:", duplicate_count(numbers))
