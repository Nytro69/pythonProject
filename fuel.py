def main():
    fraction = input("something")
    percent(fraction)



def percent(fraction):
        k, l = fuel(fraction)
        if l == 0:
            return False
        elif k / l == 1:
            return "F"
        elif k / l <= 0.01:
            return "E"
        else:
            return k / l * 100

def fuel(fraction):
    global k, l
    try:
        k, l = fraction.split("/")
        k = int(k)
        l = int(l)
    except ValueError:
        print("not a valid fraction")
        return False
    except ZeroDivisionError:
        print("can't divide by zero")
        return False
    except Exception:
        if k > l:
            print("fuel(x) in tank can not be greater than tank capacity(y), x/y")
            return False
    else:
        return k, l


if __name__ == "__main__":
    main()