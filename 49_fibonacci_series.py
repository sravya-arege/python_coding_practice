def fibonacci_series(terms):
    series = []
    first, second = 0, 1
    for _ in range(terms):
        series.append(first)
        first, second = second, first + second
    return series


terms = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci_series(terms))
