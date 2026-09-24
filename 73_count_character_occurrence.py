def occurrence_count(text, character):
    return text.count(character)


text = input("Enter a string: ")
character = input("Enter a character: ")
print("Occurrence count:", occurrence_count(text, character))
