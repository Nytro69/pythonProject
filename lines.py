import sys
from sys import argv

def main():
    testArg()



def testArg():
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
        print(len(lines))

if __name__ == "__main__":
    main()