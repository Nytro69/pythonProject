import csv
import english_words
import os
import random
import time

def clear_screen():
    os.system('cls')

def create_word():
    englis = english_words.get_english_words_set(['web2'], lower=True)
    w = list(englis)
    return random.sample(w, 1)[0]

def create_mask(length):
    return ['_'] * length

def initialize_attempts():
    return 8


def print_mask(char_mask):
    print(' '.join(char_mask))


def read_guess():
    while True:
        k = input("guess: ").lower().strip()
        if len(k) != 1:
            clear_screen()
            continue

        if not k.isalpha():
            print("Not a letter")
            time.sleep(1)
            clear_screen()
            continue

        return k

def update_mask(mask, guess, word):
    for i in range(len(word)):
        if guess == word[i]:
            mask[i] = guess


def show_ui(char_mask, attempts):
    print_mask(char_mask)
    print()
    print(f"Attempts: {attempts}")


def main1():
    word = create_word()
    attempts_left = initialize_attempts()
    mask = create_mask(len(word))
    typed_letters = []

    while True:
        clear_screen()
        show_ui(mask, attempts_left)
        guess = read_guess()
        if guess in typed_letters:
            print(f"you have already typed {guess}")
            time.sleep(1)
            continue
        typed_letters.append(guess)
        if guess not in word:
            attempts_left -= 1
        else:
            update_mask(mask, guess, word)
        if "_" not in mask:
            print("You win!!")
            with open("hangman_results.csv", "a", newline="\n") as file:
                simple_mask = ''.join(mask)
                simple_word = ''.join(word)
                list_result = [word, simple_mask, initialize_attempts() - attempts_left, typed_letters, 1]
                s = csv.writer(file)
                s.writerow(list_result)
            return
        if attempts_left == 0:
            with open("hangman_results.csv", "a", newline="\n") as file:
                simple_mask = ''.join(mask)
                simple_word = ''.join(word)
                list_result = [word, simple_mask, initialize_attempts(), typed_letters, 0]
                s = csv.writer(file)
                s.writerow(list_result)
            print(f"You lost, the word was {word}\n")
            return


def main2():
    clear_screen()
    with open("hangman_results.csv", "r") as f:
        reader = csv.reader(f)
        contents = list(reader)

        wins = 0
        used_attempts_ = 0
        letters_typed = contents[-1][3]
        mask = contents[-1][1]
        word = contents[-1][0]
        for i in range(len(contents)):
            used_attempts = int(contents[i][2])
            win = int(contents[i][4])
            wins += win
            used_attempts_ += used_attempts

        print(f"Word(latest): {word}")
        print(f"Mask(latest): {mask}")
        print(f"Letters typed(latest): {letters_typed.join(', ')}")
        print(f"Used attempts(all time): {used_attempts_}")
        print(f"Average amount of tries: {used_attempts_ / len(contents)}")
        print(f"Wins: {wins}")
        print(f"Games played {len(contents)}")
        print("\n\n")






while True:
    d = input("What do you want to do?\n1 Play Hangman\n2 Show Stats\n3 Quit\n\n")
    if d == "1":
        main1()
    elif d == "2":
        main2()
    elif d == "3":
        quit()
    else:
        print("choose 1, 2 or 3")
        time.sleep(1.5)
        clear_screen()
        continue