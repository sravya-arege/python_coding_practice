def delete_at_position(numbers, position):
    if position < 0 or position >= len(numbers):
        return None
    numbers = numbers.copy()
    numbers.pop(position)
    return numbers


numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))
position = int(input("Enter zero-based position to delete: "))
result = delete_at_position(numbers, position)
print("Updated array:", result if result is not None else "Invalid position")
