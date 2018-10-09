import requests
import json

from market_maker.utils import math

GDAX_PRICE_URL      = "https://api.cryptowat.ch/markets/gdax/ethusd/price"
KRAKEN_PRICE_URL    = "https://api.cryptowat.ch/markets/kraken/ethusd/price"
BITSTAMP_PRICE_URL  = "https://api.cryptowat.ch/markets/bitstamp/ethusd/price"
URLS = [GDAX_PRICE_URL,KRAKEN_PRICE_URL,BITSTAMP_PRICE_URL]

def get_price(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('UTF-8'))
    else:
        return
    return data.get('result').get('price')


def get_avg_index(URLS):
    prices = [get_price(url) for url in URLS if get_price(url)]
    print(prices)
    avg_price = sum(prices)/len(prices)
    avg_price = math.toNearest(avg_price,0.01)
    return avg_price