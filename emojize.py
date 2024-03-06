# variables used: argv, replace(), try or if statements, remove/replace "_".
import emoji

user = input("Input:  ")

print(emoji.emojize(f"Output: {user}", language="alias"))