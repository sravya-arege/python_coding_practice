def merge_files(first_name, second_name, output_name):
    with open(first_name, "r", encoding="utf-8") as first:
        first_content = first.read()
    with open(second_name, "r", encoding="utf-8") as second:
        second_content = second.read()
    with open(output_name, "w", encoding="utf-8") as output:
        output.write(first_content)
        output.write("\n")
        output.write(second_content)


first = input("Enter the first file name: ")
second = input("Enter the second file name: ")
output = input("Enter the output file name: ")
try:
    merge_files(first, second, output)
    print("Files merged successfully.")
except FileNotFoundError:
    print("One of the input files was not found.")
