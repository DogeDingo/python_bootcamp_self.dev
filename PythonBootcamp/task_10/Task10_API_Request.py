import requests
import time
import json

url = "https://api.goprogram.ai/inspiration"

quotes = requests.get(url).json()

def quote_getter():
    x = 0
    cool_list = []
    while x < 10:
        time.sleep(5)
        cool_list.append(quotes)
        x += 1
    return cool_list

def json_quote_list(x):
    with open("inspirational_quotes.json", "w", encoding="utf-8") as file:
        jsonString = json.dumps(x, indent=3)
        file.write(jsonString)


json_quote_list(quote_getter())