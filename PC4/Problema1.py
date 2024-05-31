

import requests

try:
    url="https://api.coindesk.com/v1/bpi/currentprice.json"
    response=requests.get(url)

    # 2. Recupero la informacion como json
    json_bitcoin = response.json()

    nro_bitcoins = float(input('Digite la cantidad de bitcoin que tiene: '))

    costo_bitcoins = nro_bitcoins * json_bitcoin['bpi']['USD']['rate_float']

    print(f'"${costo_bitcoins:,.4f}')
except requests.RequestException:
    print('Error en la captura del requests.')
