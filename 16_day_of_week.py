def get_day_name(day):
    """Return the day name for a number from 1 to 7."""
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return days.get(day, "Invalid day number")


day = int(input("Enter day number (1-7): "))
print("Day:", get_day_name(day))
