import random
import string

i = 0

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def main():
        global i
        while True:
            l = random_string(6, 6)
            k = random_string(6, 6)
            if k != l:
                i += 1
                print(f"{k} {i}")
                continue
            elif k == l:
                print(f"password: {k}, tries: {i}")
                break

def random_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    letters_and_digits = string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))