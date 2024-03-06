import csv
import os

inst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

pi = [
    1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4,
    6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7,
    1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4,
    4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9,
    9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7,
    9, 8, 2, 1, 4, 8, 0, 8, 6, 5, 1, 3, 2, 8, 2, 3, 0, 6, 6, 4,
    7, 0, 9, 3, 8, 4, 4, 6, 0, 9, 5, 5, 0, 5, 8, 2, 2, 3, 1, 7,
    2, 5, 3, 5, 9, 4, 0, 8, 1, 2, 8, 4, 8, 1, 1, 1, 7, 4, 5, 0,
    2, 8, 4, 1, 0, 2, 7, 0, 1, 9, 3, 8, 5, 2, 1, 1, 0, 5, 5, 5,
    9, 6, 4, 4, 6, 2, 2, 9, 4, 8, 9, 5, 4, 9, 3, 0, 3, 8, 1, 9,
    6, 4, 4, 2, 8, 8, 1, 0, 9, 7, 5, 6, 6, 5, 9, 3, 3, 4, 4, 6
]

os.system('clear')

def write():
    global guess
    name = input("Namn: ")
    clas = input("Klass: ")
    print(">> 3.")
    score = 0
    for i in range(len(pi)):
        try:
            guess = input(">> ")
            guess = int(guess)
        except Exception:
            if guess not in inst:
                print("\ndu ska skriva en siffra")
                guess = 11

        if guess == pi[i]:
            score += 1
        else:
            break

    with open("pi_leaderboard.csv", "a", newline='') as csvfile:
        fieldnames = ['Name', 'Score', 'Class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'Score': score, 'Class': clas})

    # Print high score and highest scorer's name
    if score == 222:
        print(f"Grattis!! Nytt rekord av {name}, {clas} med {score} siffror")

    print(f"\nFel, nästa siffra var: {pi[score]}\nDitt poäng var: {score}\n")
    get_high_score()

def get_high_score():

    with open("pi_leaderboard.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        rows = list(reader)  # Convert iterator to list

    # Sort the rows based on the scores (assuming the scores are in the second column)
    rows.sort(key=lambda x: int(x[1]), reverse=True)

    # Get the top five highest scorers
    top_five = rows[:3]

    # Print the top five highest scorers
    for rank, (name, score, class_) in enumerate(top_five, start=1):
        print(f"Rank {rank}: Namn: {name} {class_}, Siffror: {score}")

write()