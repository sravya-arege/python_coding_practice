def first_occurrence(text, character):
    return text.find(character)


text = input("Enter a string: ")
character = input("Enter a character: ")
print("First occurrence index:", first_occurrence(text, character))
