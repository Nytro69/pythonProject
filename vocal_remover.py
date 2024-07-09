import requests

file = input('file(path): ').split(", ")
r = requests.post("https://vocalremover.org/joiner/", file)


print(r.text)