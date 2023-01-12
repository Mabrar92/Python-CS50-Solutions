import requests
import json



try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r=response.json()

    #print(json.dumps(r, indent=2))
    for items in r["bpi"].values():
        print(items['rate_float'])
except requests.RequestException:
    ...