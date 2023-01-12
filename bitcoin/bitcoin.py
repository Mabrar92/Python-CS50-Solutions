import requests



try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r=response.json()
    print(r)
except requests.RequestException:
    ...