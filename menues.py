from datetime import datetime


def main():
    while True:
        print_men()
        choise = read_choise()
        dispatch(choise)



def dispatch(choise):
    if choise == 1:
        quit()
    if choise == 2:
        print_date()
    if choise == 3:
        print_joke()
    if choise == 4:
        print_hi()

def print_hi():
    print("hi")

def print_joke():
    print("What a wall says to another wall? See you in the corner")
def print_date():
    time = datetime.today().strftime('%Y-%m-%d')
    print(f"today is {time}")
def print_men():
    print("1- Quit")
    print("2- What day is today?")
    print("3- Tell me a joke")
    print("4- say hi")

def read_choise():
    choise = input("Input: ")
    return int(choise)


main()