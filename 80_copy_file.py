def copy_file(source_name, destination_name):
    with open(source_name, "r", encoding="utf-8") as source:
        content = source.read()
    with open(destination_name, "w", encoding="utf-8") as destination:
        destination.write(content)


source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")
try:
    copy_file(source, destination)
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
