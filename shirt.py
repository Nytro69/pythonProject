import sys
from sys import argv
from PIL import Image

photoFormats = [".jpeg", ".jpg", ".png"]

def main():
    testArg()

def testArg():
    try:
        first = Image.open(argv[1])
    except Exception:
        if len(argv) > 3:
            sys.exit("To few command-line arguments")
        if len(argv) < 3:
            sys.exit("to many command-line arguments")
        if argv[2].endswith(tuple(photoFormats)) == False or argv[1].endswith(tuple(photoFormats)) == False:
            sys.exit("file needs to end with, .jpeg, .jpg or .png")
    except FileNotFoundError:
        sys.exit("File not found")
    else:




if __name__ == "__main__":
    main()