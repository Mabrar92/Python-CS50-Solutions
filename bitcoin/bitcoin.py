import requests
import json



try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r=response.json()


    for items in r["bpi"].values():
        if items['code']=='USD':
            print(items['rate_float'])
except requests.RequestException:
    ...