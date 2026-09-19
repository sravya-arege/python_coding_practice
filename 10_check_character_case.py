def check_case(character):
    """Return whether an alphabet character is uppercase or lowercase."""
    if len(character) != 1 or not character.isalpha():
        return "Enter a single alphabet character"

    if character.isupper():
        return "Uppercase"
    return "Lowercase"


character = input("Enter a character: ")
print(check_case(character))
