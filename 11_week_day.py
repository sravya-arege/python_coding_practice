def get_weekday(day):
    """Return the weekday name for numbers 1 through 7."""
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return weekdays.get(day, "Invalid day number")


day = int(input("Enter week number (1-7): "))
print("Day:", get_weekday(day))
