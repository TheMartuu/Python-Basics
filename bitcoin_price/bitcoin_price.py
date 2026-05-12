import requests
import datetime
import json 

endpoint = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
price  = json.loads(requests.get(endpoint).text)
current_date = datetime.datetime.now()

converted_price = float(price["price"])

print(f"Current Bitcoin value at {current_date.strftime("%A")} {current_date.strftime("%d-%m-%Y %H:%M")}:\n$1 BTC = U$S {converted_price}.-")
