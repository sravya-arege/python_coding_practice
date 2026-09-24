def count_character_types(text):
    alphabets = sum(character.isalpha() for character in text)
    digits = sum(character.isdigit() for character in text)
    special = len(text) - alphabets - digits
    return alphabets, digits, special


text = input("Enter a string: ")
alphabets, digits, special = count_character_types(text)
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special characters:", special)
