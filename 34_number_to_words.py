ONES = [
    "Zero", "One", "Two", "Three", "Four",
    "Five", "Six", "Seven", "Eight", "Nine",
]

TEENS = [
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
]

TENS = [
    "", "", "Twenty", "Thirty", "Forty",
    "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
]


def under_thousand_to_words(number):
    """Convert a number from 0 to 999 into words."""
    words = []

    if number >= 100:
        words.append(ONES[number // 100])
        words.append("Hundred")
        number %= 100

    if 10 <= number <= 19:
        words.append(TEENS[number - 10])
    elif number >= 20:
        words.append(TENS[number // 10])
        if number % 10:
            words.append(ONES[number % 10])
    elif number > 0:
        words.append(ONES[number])

    return " ".join(words)


def number_to_words(number):
    """Convert an integer from 0 to 999,999 into words."""
    if number == 0:
        return "Zero"

    if number < 0:
        return "Minus " + number_to_words(-number)

    parts = []

    thousands = number // 1000
    remainder = number % 1000

    if thousands:
        parts.append(under_thousand_to_words(thousands))
        parts.append("Thousand")

    if remainder:
        parts.append(under_thousand_to_words(remainder))

    return " ".join(parts)


number = int(input("Enter a number (0-999999): "))

if abs(number) > 999999:
    print("Please enter a number between -999999 and 999999.")
else:
    print("In words:", number_to_words(number))
