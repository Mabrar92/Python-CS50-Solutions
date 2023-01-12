import requests



try:
    response = requests.response https://api.coindesk.com/v1/bpi/currentprice.json
except requests.RequestException:
    ...