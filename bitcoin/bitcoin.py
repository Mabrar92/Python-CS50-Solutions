import requests
import json



try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r=response.json()

    #print(json.dumps(r, indent=2))
    for items in r["bpi"]:
        print(items["USD"].values())
except requests.RequestException:
    ...