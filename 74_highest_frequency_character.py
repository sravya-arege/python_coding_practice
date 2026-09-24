def highest_frequency_character(text):
    counts = character_frequencies(text)
    return max(counts, key=counts.get) if counts else None


def character_frequencies(text):
    return {character: text.count(character) for character in set(text) if not character.isspace()}


text = input("Enter a string: ")
result = highest_frequency_character(text)
print("Highest-frequency character:", result if result else "No characters")
