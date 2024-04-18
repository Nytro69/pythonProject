from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()

def main():
    if testargv():
        font()
    elif len(sys.argv) == 1:
        random_font()
    else:
        print("error")
        quit()


def testargv():
    if len(sys.argv) >= 2 and len(sys.argv) <= 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("invalid usage")
        else:
            if sys.argv[2] not in fonts:
                sys.exit("font does not exist")
            else:
                return True
    elif len(sys.argv) != 1:
        sys.exit("invalid usage")
    else:
        return False

def font():
    user = "nigger"
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(user))


def random_font():
    user = "ham cheese and boobies let me suck those tiddies"
    rand = random.choice(figlet.getFonts())
    figlet.setFont(font=rand)
    print(figlet.renderText(user))


main()