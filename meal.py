valid_mins = []
time = input("What's the time? ").lower()

hours, minutes = time.split(":")


hours = int(hours)
if minutes[-1: -3] == "pm":
    hours += 12
    for i in minutes:
        if i.isdigit() == True:
            valid_mins.append(i)
else:
    for i in minutes:
        if i.isdigit() == True:
            valid_mins.append(i)


strminutes = ''.join([str(element) for element in valid_mins])
minutes = int(strminutes)


if hours == 7 or (hours == 8 and minutes == "00"):
    print("breakfast time")
elif hours == 12 or (hours == 13 and minutes == "00"):
    print("lunch time")
elif hours == 18 or (hours == 19 and minutes == "00"):
    print("dinner time")
else:
    print("no meal")
