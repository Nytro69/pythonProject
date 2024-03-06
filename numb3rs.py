import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if string := re.search(r"\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b\.\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b\.\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b\.\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b ", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()