def all_occurrences(text, character):
    return [index for index, value in enumerate(text) if value == character]


text = input("Enter a string: ")
character = input("Enter a character: ")
print("Occurrence indexes:", all_occurrences(text, character))
