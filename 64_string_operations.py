def string_operations(first, second):
    comparison = "equal" if first == second else ("first is greater" if first > second else "second is greater")
    return len(first), comparison, first + second


first = input("Enter the first string: ")
second = input("Enter the second string: ")
length, comparison, concatenated = string_operations(first, second)
print("Length of first string:", length)
print("Comparison:", comparison)
print("Concatenation:", concatenated)
