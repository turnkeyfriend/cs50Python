import json
import sys
import requests

#specify as a command-line argument the number of Bitcoins
if len(sys.argv) != 2:
    sys.exit("Incorrect number of arguments.")
try:
    qty = float(sys.argv[1])
except ValueError:
    sys.exit("Invalid argument")
    
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

dbase = response.json()
per = dbase["bpi"]["USD"]["rate"]
per = per.replace(",", "")
total = float(per) * float(sys.argv[1])

print(f"${total:,.4f}")
