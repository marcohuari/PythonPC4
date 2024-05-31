
import requests
import os

##Me dirigo a la ruta del Problema4
os.chdir('/workspaces/PythonPC4/PC4/Problema4')

url="https://api.coindesk.com/v1/bpi/currentprice.json"
response=requests.get(url)

# 2. Recupero la informacion como json
json_bitcoin = response.json()

print(json_bitcoin['bpi'])

bitcoin_usd = str(json_bitcoin['bpi']['USD']['rate_float'])
bitcoin_gbp = str(json_bitcoin['bpi']['GBP']['rate_float'])
bitcoin_eur = str(json_bitcoin['bpi']['EUR']['rate_float'])

with open('bitcoin.txt','w') as f:
    data = f.write(f'Bitcoin USD: {bitcoin_usd}')
    data = f.write('\n')
    data = f.write(f'Bitcoin GBP: {bitcoin_gbp}')
    data = f.write('\n')
    data = f.write(f'Bitcoin EUR: {bitcoin_eur}')

print(data)