import requests


def coin_details():  # This function prints the all time high and the date when it reached the all time high
    id = input("Please enter the name of the crypto currency for which you want the detais:\n").lower()
    value_in = input("Please enter the currency in which you would want to see the price of "f"{id}?" " USD, EUR, GBP, PLN or INR\n")
    url = f"https://api.coingecko.com/api/v3/coins/{id}"

    response1 = requests.get(url=url)
    all_time_high = response1.json()["market_data"]["ath"][value_in]
    all_time_high_date = response1.json()["market_data"]["ath_date"][value_in]
    print(f"The all time high for {id.capitalize()} is {all_time_high:,} {value_in.upper()} which was created on {all_time_high_date.split('T')[0]}")
