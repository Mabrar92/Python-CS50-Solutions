import requests
import json
import sys



try:
    if len(sys.argv) < 2:
        sys.exit("Missing Command Line Argument")
    elif len(sys.argv) == 2:
            if float(sys.argv[1]) :
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                r=response.json()
                for items in r["bpi"].values():
                    if items['code']=='USD':
                        a = float(sys.argv[1]) * items['rate_float']
                        print(f"${a:,.4f}")

            else:
                sys.exit("Command Line Argument is not a number")


except requests.RequestException:
    ...
except ValueError:
     sys.exit("Command Line Argument is not a number")