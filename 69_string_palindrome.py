def is_palindrome(text):
    cleaned = "".join(character.lower() for character in text if character.isalnum())
    return cleaned == cleaned[::-1]


text = input("Enter a string: ")
print("Palindrome" if is_palindrome(text) else "Not palindrome")
