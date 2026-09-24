def count_words(text):
    return len(text.split())


text = input("Enter a string: ")
print("Word count:", count_words(text))
