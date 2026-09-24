def character_frequencies(text):
    counts = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    return counts


text = input("Enter a string: ")
print("Character frequencies:", character_frequencies(text))
