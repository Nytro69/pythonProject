# think it recursively
def str_reverse(s):
    if len(s) <= 1:
        return s

    m = len(s) // 2

    half1 = str_reverse(s[:m])

    half2 = str_reverse(s[m:])


    return half2 + half1

if __name__ == "__main__":
    print(str_reverse("base"))