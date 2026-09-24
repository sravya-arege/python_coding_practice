def is_perfect(number):
    if number < 2:
        return False
    divisor_sum = 1
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            divisor_sum += divisor
            if divisor != number // divisor:
                divisor_sum += number // divisor
    return divisor_sum == number


number = int(input("Enter a number: "))
print("Perfect" if is_perfect(number) else "Not perfect")
