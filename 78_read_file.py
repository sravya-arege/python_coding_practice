def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


filename = input("Enter the file name: ")
try:
    print(read_file(filename))
except FileNotFoundError:
    print("File not found.")
