def duplicate_count(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return sum(count > 1 for count in counts.values())


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Number of duplicate values:", duplicate_count(numbers))
