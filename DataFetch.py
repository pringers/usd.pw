import config
import json
import requests

def loadForFile(filename):
    f = open(filename, "r")
    dat = json.load(f)
    f.close()
    return dat

def pullPriceDataForSymbol(sym):
    '''
    sym = Symbol for Conversion.  Because all currencies are converted in 
              relation to Bitcoin, we are just going to pull XXXBTC.json,
              where `xxx` is the symbol parameter.
    '''

    if not sym in config.SUPPORTED_SYMBOLS:
        return None

    filename = "./endpoints/" + sym + "BTC.json"
    ret = []
    try:
        dat = loadForFile(filename)
    except Exception:
        print("Failed to load endpoints for symbol " + sym)
        return None
    for endpoint in dat:
        if config.DEBUG:
            print("Fetching for " + endpoint["name"])
        j = requests.get(endpoint["address"]).json()
        pr = j
        for i in endpoint["location"]:
            pr = pr[i]
        pr = float(pr) ** endpoint["power"]
        ret.append(pr)
    return ret

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
