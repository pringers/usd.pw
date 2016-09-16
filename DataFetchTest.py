# Run as python DataFetchTest.py
import DataFetch
print(DataFetch.pullPriceDataForSymbol('USD'))
print(DataFetch.pullPriceDataForSymbol('LTC', sym2 = 'USD'))
