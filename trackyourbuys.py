import requests


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
    params = {
        "portfolio": {
            "cryptocurrency": crypto_name,
            "amount": amount,
            "price": price,
            "date": date,
            "exchange": exchange,
        }
    }
    requests.post(url=url, headers=header, json=params)
    print("Thank you!")
