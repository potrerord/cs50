import json
import requests

# Uncomment this and add your own key for the pset:
KEY = "ZPTEVGH1DYQAZ1R6"


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the date and price table described in the pset.

    print()

    # Get user input.
    symbol = input("Enter a stock symbol: ")
    print()

    # Get list of daily close prices for past hundred days.
    dates_prices = get_quotes(symbol)

    # Print report.
    print(f"Last hundred days price data for {symbol.upper()}:")
    for day in dates_prices:
        print(f"{day[0]} {day[1]}")

    print()


def build_url(symbol):
    """Build URL for Alpha Vantage API."""

    url = "https://www.alphavantage.co/query?"
    url += f"function=TIME_SERIES_DAILY"
    url += f"&symbol={symbol}"
    url += f"&outputsize=compact"
    url += f"&datatype=json"
    url += f"&apikey={KEY}"
    return url


def get_quotes(symbol):
    """
    Take a stock symbol and return a list of tuples with the date and
    closing price for the last hundred days, for example,
    [ ('2022-07-15', '256.7200'), ('2021-07-15', '254.0800'), ... ]
    """

    # Build URL for API request.
    url = build_url(symbol)

    # Make API request to Alpha Vantage.
    data = requests.get(url).json()

    # Make list of tuples with date and closing price of each day.
    days = data["Time Series (Daily)"]
    dates_prices = []
    for day in days:
        price = f"${round(float(days[day]['4. close']), 2):.2f}"
        dates_prices.append((day, price))

    return dates_prices

if __name__ == "__main__":
    main()
