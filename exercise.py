sentance = input("Sentance: ")

words = sentance.split(" ")

validwords = []

for word in words:
    if word != "":
        validwords.append(word)

for word in validwords:
    print(word)
