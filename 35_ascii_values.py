def print_ascii_values():
    """Print printable ASCII characters and their numeric values."""
    for value in range(32, 127):
        print(f"{value:3} : {chr(value)}")


print_ascii_values()
