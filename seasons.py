import operator
import datetime
import re
import sys


def main():
    y = datetime.date.today()

    x = input("Date: ")
    if re.search(r"[0-9]{4}-(1[0-2]│0[1-9])-(3[0-1]│[0-2][0-9])", x):
        ...

    else:
        sys.exit("Invalid Date")




main()