import json
import requests

# Uncomment this and add your own key for the pset:
KEY = "ZPTEVGH1DYQAZ1R6"


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the date and price table described in the pset.

    symbol = input("Enter a stock symbol: ")

    # Build URL for API request.
    url = build_url(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={KEY}")

    # Make API request to Alpha Vantage.
    data = requests.get(url).json()

    print(data)



    requests.get(url).json()

    print(f"Last hundred days price data for {symbol}:")
    for i in thing:
        print(f"{date} {price}")

# Build your api url here. See
# https://www.alphavantage.co/documentation/#dailyadj
# do decide what values to add for the parameters.
def build_url(symbol):
    url = "https://www.alphavantage.co/query?"
    url += "function=???"
    url += "&symbol=???"
    url += "&apikey=???"
    return url

# Use this API url with your key and symbol
def get_quotes(symbol):
    """
    Takes a stock symbol and returns a list of tuples with the date
    and closing price for the last hundred days, for example,
    [ ('2022-07-15', '256.7200'), ('2021-07-15', '254.0800'), ... ]
    """
    # Add your code here


if __name__ == "__main__":
    main()
