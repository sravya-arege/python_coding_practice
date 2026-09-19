def print_alphabets():
    """Print lowercase English alphabets from a to z."""
    character = ord("a")

    while character <= ord("z"):
        print(chr(character), end=" ")
        character += 1

    print()


print_alphabets()
