#Ignore this code 

# The function below returns the hour, minute and period of a specific time in 24 hour format
# the hour and minute values are integers while the period values are strings
# The returned value will be in a list e.g 2.pm will be returned as [14,00,"pm"] e.t.c
'''
def time_format(hour,minute,period):
    time = []
    if (hour == 12 and period == "am"):
        hour = 00
        time = [hour,minute,period]
        return time
    elif hour == 1 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 2 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 3 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 4 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 5 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 6 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 7 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 8 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 9 and period == "am":
        hour = int(str(0) + str(hour))
        time = [hour,minute,period]
        return time
    elif hour == 10 and period == "am":
        time = [hour,minute,period]
        return time
    elif hour == 11 and period == "am":
        time = [hour,minute,period]
        return time
    elif hour == 12 and period == "noon" or period == "pm":
        time = [hour,minute,"noon"]
        return time
    elif hour == 1 and period == "pm":
        hour = 13
        time = [hour,minute,period]
        return time
    elif hour == 2 and period == "pm":
        hour = 14
        time = [hour,minute,period]
        return time
    elif hour == 3 and period == "pm":
        hour = 15
        time = [hour,minute,period]
        return time
    elif hour == 4 and period == "pm":
        hour = 16
        time = [hour,minute,period]
        return time
    elif hour == 5 and period == "pm":
        hour = 17
        time = [hour,minute,period]
        return time
    elif hour == 6 and period == "pm":
        hour = 18
        time = [hour,minute,period]
        return time
    elif hour == 7 and period == "pm":
        hour = 19
        time = [hour,minute,period]
        return time
    elif hour == 8 and period == "pm":
        hour = 20
        time = [hour,minute,period]
        return time
    elif hour == 9 and period == "pm":
        hour = 21
        time = [hour,minute,period]
        return time
    elif hour == 10 and period == "pm":
        hour = 22
        time = [hour,minute,period]
        return time
    elif hour == 11 and period == "pm":
        hour = 23
        time = [hour,minute,period]
        return time
    elif hour == 12 and period == "midnight":
        hour = 12
        time = [hour,minute,period]
        return time

    mess = time_format(12,00,"pm")
    print(mess)
'''