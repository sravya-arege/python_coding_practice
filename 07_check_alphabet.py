def check_alphabet(character):
    """Return whether the given character is an alphabet."""
    if len(character) != 1:
        return "Enter exactly one character"
    if ("a" <= character <= "z") or ("A" <= character <= "Z"):
        return "Alphabet"
    return "Not an Alphabet"


character = input("Enter a character: ")
print(check_alphabet(character))
