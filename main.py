import requests
from datetime import date
import coinlist

#There was no need of an API key as this is a free version of the CoinGiecko API


print("Welcome to the CryptoView!")
flag = True
check_coinlist = input("If this is your first time here, we suggest you to check the coins that you can get data for. Press y to get the list or any other button to conitue:\n").upper()

if check_coinlist == "Y":
    print(coinlist.coin_name)

def coin_price():  #This function returns the current price of the Cryptocurrency
    url = "https://api.coingecko.com/api/v3/simple/price"

    coin = input("Please enter the name of  the coin? Example: Bitcoin, Ethereum etc. \n").lower()
    value_in = input("Please enter the currency in which you would want to see the price of "f"{coin}" " USD, EUR, GBP, PLN or INR\n")
    parameters = {
        "ids": coin,
        "vs_currencies": value_in

    }

    response = requests.get(url=url, params=parameters)
    data=response.json()[coin][value_in]
    print(f"{value_in.upper()} {data:,}")


def coin_details():  # This function prints the all time high and the date when it reached the all time high
    id = input("Please enter the name of the crypto currency for which you want the detais:\n").lower()
    value_in = input("Please enter the currency in which you would want to see the price of "f"{id}?" " USD, EUR, GBP, PLN or INR\n")
    url = f"https://api.coingecko.com/api/v3/coins/{id}"

    response1 = requests.get(url=url)
    all_time_high = response1.json()["market_data"]["ath"][value_in]
    all_time_high_date = response1.json()["market_data"]["ath_date"][value_in]
    print(f"The all time high for {id.capitalize()} is {all_time_high:,} {value_in.upper()} which was created on {all_time_high_date.split('T')[0]}")


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

def track_your_buys(): #This function keeps a record of your crypto buys.
    url = "https://api.sheety.co/51a52c92077ec932ccd83cdf4e854ae4/portfolioTracker/portfolio"
    crypto_name = input("Please enter the name of the crypto currenncy that you bought?\n")
    amount = input("Please enter the amount that you bought?\n")
    price = input("What was the price of the cryptocurrency?\n")
    date = input("Please enter the date when you made the buy(DD-MM-YYYY)?\n")
    exchange = input("Which exchange did you use to buy this crypto currency?\n")
    header = {
        "Content-Type": "application/json"
    }
    params={
        "portfolio":{
            "cryptocurrency": crypto_name,
            "amount": amount,
            "price": price,
            "date": date,
            "exchange": exchange,
        }
    }
    requests.post(url=url, headers=header, json=params)
    print("Thank you!")


while flag:
    print("Please enter a number according to the choices below")
    user_choice = input("1. Check the price of a coin\n2. Know the highest price a coin has reached\n3. Check the market capitilicazation of a coin\n"
                        "4. Save your latest buy into a google sheet\n")

    choices = {
        "1": coin_price,
        "2": coin_details,
        "3": marketcap,
        "4": track_your_buys
    }
    choices[user_choice]()

    try_again = input("Press Y to try another function, Press any other button to finish.\n").upper()
    if try_again == "Y":
        flag = True
    else:
        flag = False

