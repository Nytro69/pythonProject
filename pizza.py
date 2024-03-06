import csv
from sys import argv
import sys
import tabulate

try:
    file = open(argv[1], "r")
except Exception:
    if len(argv) > 2:
        sys.exit("To many arguments")
    if len(argv) < 2:
        sys.exit("to few arguments")
except FileNotFoundError:
    sys.exit("File not found")
else:
    lines = file.readlines()
    headerNot = lines[0]
    tableNot = lines[1:]
    header = headerNot.split(",")
    table = []

    for i in range(len(tableNot)):
        f = tableNot[i].split(",")
        table.append(f)

    print(tabulate.tabulate(table, header, tablefmt="grid"))
