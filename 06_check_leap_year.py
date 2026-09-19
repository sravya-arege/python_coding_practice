def check_leap_year(year):
    """Return whether the given year is a leap year."""
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return "Leap Year"
    return "Not a Leap Year"


year = int(input("Enter a year: "))
result = check_leap_year(year)

print("Result:", result)
