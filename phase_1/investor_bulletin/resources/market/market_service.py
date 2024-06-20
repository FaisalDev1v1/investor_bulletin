""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""



import requests

API_KEY = "a36fff32b6e84b0b97e7f3d1eb164cf2"
BASE_URL = "https://api.twelvedata.com/time_series?"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}
SYMBOLS = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]

def get_market_prices():
    prices = {}
    for symbol in SYMBOLS:
        response = requests.get(BASE_URL, headers=HEADERS, params={
            "symbol": symbol,
            "interval": "1min",
            "outputsize": "1"
        })
        if response.status_code == 200:
            data = response.json()
            prices[symbol] = data['values'][0]['close']
        else:
            raise Exception(f"Error retrieving data for {symbol}: {response.text}")
    return prices
