def lowest_frequency_character(text):
    counts = character_frequencies(text)
    return min(counts, key=counts.get) if counts else None


def character_frequencies(text):
    return {character: text.count(character) for character in set(text) if not character.isspace()}


text = input("Enter a string: ")
result = lowest_frequency_character(text)
print("Lowest-frequency character:", result if result else "No characters")
