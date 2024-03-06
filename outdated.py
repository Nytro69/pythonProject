months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

def main():
    global month, day, year
    month, day, year = spliting()
    print(f"{year}-{month}-{day}")

def spliting():
    while True:
        try:
            user = input("Date: ").strip().lower()
            if '/' in user:
                i, day, year = user.split('/')
                i = int(i)
                day = int(day)
                year = int(year)
                if day > 31 or day < 1:
                    continue
                elif i > 12 or i < 1:
                    continue
            else:
                month, day, year = user.split(' ')
                if month in months:
                    day = int(day)
                    if day > 31 or day < 1:
                        continue
                    else:
                        month = month.replace(",", "")
                        year = int(year)
                        for i in range(len(months)):
                            if month == months[i]:
                                i = i + 1

                else:
                    continue
        except ValueError:
            pass

        return i, day, year

if __name__ == '__main__':
    main()