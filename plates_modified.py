existing_plates = ["RIEF", ]

import random
import string

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if high(s):
        if first_chars(s):
            if middle_detect(s):
                if punctuation(s):
                    if first_int_zero(s):
                        if exist(s):
                            return True
                        else:
                            print("already taken")
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


# might not
def first_int_zero(s):
    for i in range(len(s)):
        if s[i] == "0" and s[i - 1] in alphabet:
            return False
    else:
        return True


# clear
def punctuation(s):
    if " " in s or "." in s or "," in s:
        return False
    else:
        return True


# might not
def middle_detect(s):
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1] in alphabet:
            return False
    else:
        return True



# clear
def first_chars(s):
    if s[0] in alphabet and s[1] in alphabet:
        return True
    else:
        return False


# clear
def high(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def exist(s):
    if s in existing_plates:
        return False

main()
