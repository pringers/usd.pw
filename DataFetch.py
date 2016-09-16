import config
import json
import requests

def loadForFile(filename):
    f = open(filename, "r")
    dat = json.load(f)
    f.close()
    return dat

def pullPriceDataForSymbol(sym, sym2='BTC'):
    '''
    sym  = Symbol for Conversion.  Because all currencies are converted in 
              relation to Bitcoin, we are just going to pull XXXBTC.json,
              where `xxx` is the symbol parameter.
    sym2 = Secondary Symbol.  Should not be used except in edge cases.
    '''

    if not (sym in config.SUPPORTED_SYMBOLS and sym2 in config.TARGET_SYMBOLS):
        return None

    if sym  == sym2:
        return [1]
    
    filename = "./endpoints/" + sym + sym2 + ".json"
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
