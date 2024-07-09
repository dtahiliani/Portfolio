import json
from urllib.request import urlopen

#yahoo finance currency conversion API
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()
    
print(source)
