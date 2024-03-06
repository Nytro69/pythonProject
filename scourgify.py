from sys import argv
import sys

try:
    file = open(argv[1], "r")
except Exception:
    if len(argv) > 3:
        sys.exit("To many arguments")
    if len(argv) < 3:
        sys.exit("to few arguments")
except FileNotFoundError:
    sys.exit("File not found")
else:
    k = file.read()
    k = k.replace('"', '')
    k = k.replace(" ", "")
    f = open(argv[2], "w")
    f.write(k)