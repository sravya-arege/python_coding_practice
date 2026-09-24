def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


filename = input("Enter the file name: ")
content = input("Enter the content: ")
write_file(filename, content)
print("File written successfully.")
