def last_occurrence(text, character):
    return text.rfind(character)


text = input("Enter a string: ")
character = input("Enter a character: ")
print("Last occurrence index:", last_occurrence(text, character))
