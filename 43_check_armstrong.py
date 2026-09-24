def is_armstrong(number):
    digits = str(abs(number))
    total = sum(int(digit) ** len(digits) for digit in digits)
    return number >= 0 and total == number


number = int(input("Enter a number: "))
print("Armstrong" if is_armstrong(number) else "Not Armstrong")
