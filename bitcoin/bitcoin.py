import requests
import json
import sys



try:
    if len(sys.argv) < 2:
        sys.exit("Missing Command Line Argument")
    elif len(sys.argv) == 2:
        if sys.argv[1].isnumeric() :
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            r=response.json()
            for items in r["bpi"].values():
                if items['code']=='USD':
                    print(f"{sys.argv[1] * items['rate_float']:,.4f}")

        else:
            sys.exit("Command Line Argument is not a number")


except requests.RequestException:
    ...