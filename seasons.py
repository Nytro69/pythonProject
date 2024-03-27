import datetime
from str_reverse import str_reverse

class Day:
    number = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: ""
    }
    number_10 = {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninty",
        0: ""
    }

    number_3 = {
        3: "hundred",
        6: "twenty",
        9: "thirty",
        12: "forty",
        15: "fifty",
        18: "sixty",
        21: "seventy",
        24: "eighty",
        27: "ninty"
    }

    def __init__(self):
        self.date = input("Date: ")

    def age_difference(self):
        today = datetime.date.today()
        year, month, day = self.date.split("-")
        y = datetime.date(int(year), int(month), int(day))
        difference_day = (today - y).days
        difference_sec = difference_day * 24 * 60 * 60

        return difference_sec

    def textify(self, df):
        self.df = df
        print(self.df)
        k = []
        x = 1
        for i in range(len(list(str(self.df))), 3):
            ...


        print(k)



z = Day()
print(z.textify(z.age_difference()))