import requests


def create_exchage_rate_url(source_currency, target_currency):
    return f"https://api.forex.se/currency/exchangeRates/SWE-{source_currency.upper()}-{target_currency.upper()}"

def get_exchange_rate(source_currency, target_currency):
    url = create_exchage_rate_url(source_currency, target_currency)
    response = requests.get(url)
    return response.json()['data']['attributes']['rate']


def run():
    source = input('source currency: ')
    amount = float(input('amount: '))
    target = input('target currency: ')

    exchange_rate = get_exchange_rate(source, target)
    amount_received = amount / exchange_rate
    print(f"For {amount:.4f} {source} you get {amount_received:.4f} {target}")


