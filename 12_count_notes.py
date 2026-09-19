def count_notes(amount):
    """Print note counts and return the total number of notes."""
    denominations = [2000, 500, 200, 100, 50, 20, 10]
    total_notes = 0

    for note in denominations:
        count = amount // note
        if count > 0:
            print(f"₹{note}: {count} notes")

        total_notes += count
        amount %= note

    return total_notes


amount = int(input("Enter amount: "))
result = count_notes(amount)

print("Total number of notes:", result)
