dictonary_answers = {
    1: 12,
    2: 89,
    "etc": "later",
}

que = int(input("what question are you on? "))

ans = int(input("what's your answer? "))

if dictonary_answers[que] == ans:
    print(f"correct, the answer is {dictonary_answers[que]}")
else:
    print(f"incorrect, the answer is {dictonary_answers[que]}")