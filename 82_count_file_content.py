def count_file_content(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    return len(content), len(content.split()), len(content.splitlines())


filename = input("Enter the file name: ")
try:
    characters, words, lines = count_file_content(filename)
    print("Characters:", characters)
    print("Words:", words)
    print("Lines:", lines)
except FileNotFoundError:
    print("File not found.")
