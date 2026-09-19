def digit_frequency(number):
    """Return the frequency of digits 0 through 9."""
    number = abs(number)
    frequency = [0] * 10

    if number == 0:
        frequency[0] = 1
        return frequency

    while number > 0:
        digit = number % 10
        frequency[digit] += 1
        number //= 10

    return frequency


number = int(input("Enter a number: "))
frequency = digit_frequency(number)

for digit, count in enumerate(frequency):
    if count > 0:
        print(f"{digit}: {count}")
