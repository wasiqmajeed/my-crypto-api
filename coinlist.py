import requests

coin_name = []
params = {
    "vs_currency":"usd",
    "order": "market_cap_desc",
    "per_page": 100
}
response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params=params)
coin_list = response.json()

for coins in coin_list:
    coin_name.append(coins['id'])
