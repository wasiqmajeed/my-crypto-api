import requests
from datetime import date

def marketcap():  # This function prints the current marketcap of a specific coin
    id = input("Please enter the name of the crypto currency\n").lower()
    value_in = input("Please enter the currency in which you would want to see the price of "f"{id}" " USD, EUR, GBP, PLN or INR\n")
    url = f"https://api.coingecko.com/api/v3/coins/{id}/history"

    parameters = {
        "date": date.today().strftime('%d-%m-%Y')
    }
    response = requests.get(url=url, params=parameters)
    data = response.json()["market_data"]["market_cap"][value_in]
    print(f'{value_in.upper()} {data:,}')