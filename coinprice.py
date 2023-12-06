import requests


def coin_price():  #  This function returns the current price of the Cryptocurrency
    url = "https://api.coingecko.com/api/v3/simple/price"
    try:
        coin = input("Please enter the name of  the coin? Example: Bitcoin, Ethereum etc. \n").lower()
        value_in = input(
            "Please enter the currency in which you would want to see the price of "f"{coin}" " USD, EUR, GBP, PLN or INR\n")
        parameters = {
            "ids": coin,
            "vs_currencies": value_in

        }
        response = requests.get(url=url, params=parameters)
        data = response.json()[coin][value_in]
        print(f"{value_in.upper()} {data:,}")
    except KeyError:
        print("Coin or Currency not in the list, please try again")


