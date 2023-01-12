import requests



try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.json()
    print(response)
except requests.RequestException:
    ...