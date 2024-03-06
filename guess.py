import random

number = random.randrange(1,100)

i = 1

while True:

    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("That's not an int!")
        continue

    if guess == number:
        print(f"You won, in {i} attempts")
        break

    if guess < number:
        print("Too small")
    else:
        print("Too large")
    i += 1
