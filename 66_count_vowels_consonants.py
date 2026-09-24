def count_vowels_consonants(text):
    vowels = sum(character.lower() in "aeiou" for character in text if character.isalpha())
    consonants = sum(character.isalpha() and character.lower() not in "aeiou" for character in text)
    return vowels, consonants


text = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(text)
print("Vowels:", vowels)
print("Consonants:", consonants)
