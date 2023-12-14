# The function below returns the hour, minute and period of a specific time in 24 hour format
# the hour and minute values are integers while the period values are strings
# The returned value will be in a list e.g 2.pm will be returned as [14,00,"pm"] e.t.c
def convert_time(hour, minute, period):
    time = []

    if period == "noon":
        hour = 12
    elif period == "midnight":
        hour = 0
    elif period == "am" and hour == 12:
        hour = 0
    elif period == "pm" and hour == 12:
        hour = 12
    elif period == "am" and hour > 12:
        hour -= 12
    elif period == "pm" and hour < 12:
        hour += 12

    time = [hour, minute, period]
    return time
mess = convert_time(12,00,"pm")
print(mess)

