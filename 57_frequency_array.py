def frequencies(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
print("Frequencies:", frequencies(numbers))
