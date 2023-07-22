import csv
import datetime
import pytz
import requests
import subprocess
from typing import Dict
import urllib
import uuid

import flask
import functools

"""
from flask import redirect, render_template, session
from functools import wraps
"""


def apology(message, code=400):
    """Render message as an apology to the user."""

    def escape(s):
        """Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """

        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return flask.render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """Decorate functions to require login before accessing routes.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """

    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        """Redirect user to login if current session has no user_id."""

        if flask.session.get("user_id") is None:
            return flask.redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def lookup(symbol: str) -> Dict:
    """Look up quote for stock symbol argument."""

    # Prepare API request with stock symbol, current time, and start time.
    symbol = symbol.upper()
    end = datetime.datetime.now(pytz.timezone("US/Eastern"))
    start = end - datetime.timedelta(days=7)

    # Yahoo Finance API
    url = (
        f"https://query1.finance.yahoo.com/v7/finance/download/{urllib.parse.quote_plus(symbol)}"
        f"?period1={int(start.timestamp())}"
        f"&period2={int(end.timestamp())}"
        f"&interval=1d&events=history&includeAdjustedClose=true"
    )

    # Query API
    try:
        response = requests.get(
            url,
            cookies={"session": str(uuid.uuid4())},
            headers={"User-Agent": "python-requests", "Accept": "*/*"},
        )
        response.raise_for_status()

        # CSV header: Date,Open,High,Low,Close,Adj Close,Volume
        quotes = list(csv.DictReader(response.content.decode("utf-8").splitlines()))
        quotes.reverse()
        price = round(float(quotes[0]["Adj Close"]), 2)

        # Return dictionary
        return {"name": symbol, "price": price, "symbol": symbol}
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
