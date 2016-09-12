import json
import requests

def loadForFile(filename):
    f = open(filename, "r")
    dat = json.load(f)
    f.close()
    return dat

if __name__ == "__main__":
    items = loadForFile("./endpoints/BTC-USD.json")
    for i in items:
        j = requests.get(i).json()
        found = False
        for l in ['last', 'last_price', 'price']:
            if l in j:
                found = True
                print(j[l])
        if not found:
            for k in ['btc_usd', 'USDT_BTC']:
                if k in j:
                    print(j[k]['last'])
        raw_input()
