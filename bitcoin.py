import requests
import sys

def main():
    requesttest()

def requesttest():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("to many command line arguments")

    try:
        bit = float(sys.argv[1])
    except ValueError:
        sys.exit("not an int")
    else:
        try:
            r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            o = r.json()
            rate = o["bpi"]["USD"]["rate_float"]
            float(rate)
            add = int(sys.argv[1])
            sum = rate * add
            print(f"exchange: $ {sum:,.4f}")
        except requests.RequestException as i:
            sys.exit(f"Error: {i}")


main()