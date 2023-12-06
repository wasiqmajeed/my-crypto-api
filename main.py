import coinlist
from coinprice import coin_price
from coindetails import coin_details
from marketcap import marketcap
from trackyourbuys import track_your_buys
#There was no need of an API key as this is a free version of the CoinGiecko API


print("Welcome to the CryptoView!")
flag = True
check_coinlist = input("If this is your first time here, we suggest you to check the coins that you can get data for. Press y to get the list or any other button to conitue:\n").upper()

if check_coinlist == "Y":
    print(coinlist.coin_name)

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

