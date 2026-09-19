def check_character(character):
    """Classify a character as alphabet, digit, or special character."""
    if len(character) != 1:
        return "Enter exactly one character"

    if character.isalpha():
        return "Alphabet"
    if character.isdigit():
        return "Digit"
    return "Special Character"


character = input("Enter a character: ")
print(check_character(character))
