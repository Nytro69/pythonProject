import csv

with open("questions.csv", "a") as file:
    fieldnames = ['Question', 'Alternatives', 'Answer']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({"Question": input("Q: "), "Alternatives": input("Alt: "), "Answer": input("A: ")})

with open("questions.csv", "r") as file:
    reader = next(csv.reader(file))
    reader = list(reader)
