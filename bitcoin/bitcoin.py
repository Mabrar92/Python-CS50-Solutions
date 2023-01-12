import requests
import json
import sys



try:
    if len(sys.argv) < 2:
        sys.exit("Missing Command Line Argument")
    elif len(sys.argv) == 2:
        if sys.argv[1] is str :
            sys.exit("Command Line Argument is not a number")
        else:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            r=response.json()


            for items in r["bpi"].values():
                if items['code']=='USD':
                    print(items['rate_float'])
except requests.RequestException:
    ...