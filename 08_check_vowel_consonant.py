def check_vowel_consonant(character):
    """Return whether the character is a vowel or consonant."""
    if len(character) != 1 or not character.isalpha():
        return "Enter a single alphabet character"

    if character.lower() in "aeiou":
        return "Vowel"
    return "Consonant"


character = input("Enter a character: ")
print(check_vowel_consonant(character))
