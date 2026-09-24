def delete_at_position(numbers, position):
    if 0 <= position < len(numbers):
        return numbers[:position] + numbers[position + 1:]
    return None


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
position = int(input("Enter zero-based position to delete: "))
result = delete_at_position(numbers, position)
print("Updated array:", result if result is not None else "Invalid position")
