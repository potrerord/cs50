"""

"""


import os  # contains functions to interact with operating system

import cs50  # contains SQL setup
import flask  # micro web framework including tools/libraries/tech to build web apps with python
import flask_session  # allows you to store session data on server side
import re
import tempfile  # python standard library module to create temporary files during exec
from typing import Dict, Union
import werkzeug.security  # module in werkzeug library that provides various security functions like password hashing


import helpers

"""
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
"""

# Configure Flask application in current file.
app = flask.Flask(__name__)

# Configure Jinja environment with custom USD formatting filter.
app.jinja_env.filters["usd"] = helpers.usd

# Configure Flask to store sessions on local disk (not signed cookies).
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
flask_session.Session(app)

# Create SQL class object from CS50 library with finance.db database.
db = cs50.SQL("sqlite:///finance.db")


@app.after_request
def after_request(response: flask.Response) -> flask.Response:
    """Ensure responses aren't cached."""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@helpers.login_required
def index() -> flask.Response:
    """Show portfolio of stocks."""

    # Complete the implementation of index in such a way that it
    # displays an HTML table summarizing, for the user currently logged
    # in, which stocks the user owns, the numbers of shares owned, the
    # current price of each stock, and the total value of each holding
    # (i.e., shares times price).



    # Also display the user’s current cash balance along with a grand
    # total (i.e., stocks’ total value plus cash).



    # Odds are you’ll want to execute multiple SELECTs. Depending on how
    # you implement your table(s), you might find GROUP BY HAVING SUM
    # and/or WHERE of interest.



    # Odds are you’ll want to call lookup for each stock.







    return helpers.apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@helpers.login_required
def buy() -> flask.Response:
    """Buy shares of stock on behalf of user request."""

    # If user arrived to /buy via POST,
    if flask.request.method == "POST":
        # Verify that symbol form has input.
        form_symbol = flask.request.form.get("symbol")
        if not form_symbol:
            return helpers.apology("Missing symbol.")

        # Verify that symbol exists.
        symbol_data = helpers.lookup(form_symbol)
        if not symbol_data:
            return helpers.apology("Invalid symbol.")

        # Verify that shares has input.
        form_shares = flask.request.form.get("shares")
        if not form_shares:
            return helpers.apology("Missing shares.")

        # Verify that shares is positive integer.
        if not isinstance(form_shares, int):
            return helpers.apology("Enter valid integer.")
        elif form_shares < 1:
            return helpers.apology("Not enough shares.")

        # Get data from lookup() return.
        name = symbol_data["name"]
        symbol = symbol_data["symbol"]
        price = symbol_data["price"]

        # Get user's pre- and post-transaction cash balance.
        user_data = db.execute("SELECT * FROM users WHERE id = ?",
                                    flask.session["user_id"])
        if not user_data:
            return helpers.apology("Unknown error.")
        pre_trans_cash = user_data[0]["cash"]
        post_trans_cash = pre_trans_cash - price

        # Create transaction history table if it does not already exist.
        db.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                type TEXT NOT NULL,
                symbol TEXT NOT NULL,
                price NUMERIC NOT NULL,
                FOREIGN KEY (id) REFERENCES users(id)
            )
        """)

        # Add one or more new tables to finance.db via which to keep
        # track of the purchase. Store enough information so that you
        # know who bought what at what price and when.



        # Use appropriate SQLite types.



        # Define UNIQUE indexes on any fields that should be unique.



        # Define (non-UNIQUE) indexes on any fields via which you will
        # search (as via SELECT with WHERE).



        # Render an apology, without completing a purchase, if the user
        # cannot afford the number of shares at the current price.



        # You don’t need to worry about race conditions (or use
        # transactions).



        # Once you’ve implemented buy correctly, you should be able to see
        # users’ purchases in your new table(s) via phpLiteAdmin or sqlite3.




        # Redirect to homepage with updated info.
        return flask.redirect("/")

    # If user arrived to /buy via GET, render buy form.
    else:
        return flask.render_template("buy.html")


@app.route("/history")
@helpers.login_required
def history() -> flask.Response:
    """Show history of transactions."""


    """Complete the implementation of history in such a way that it displays an HTML table summarizing all of a user’s transactions ever, listing row by row each and every buy and every sell.

    For each row, make clear whether a stock was bought or sold and include the stock’s symbol, the (purchase or sale) price, the number of shares bought or sold, and the date and time at which the transaction occurred.
    You might need to alter the table you created for buy or supplement it with an additional table. Try to minimize redundancies.
    """










    return helpers.apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login() -> flask.Response:
    """Log user in."""

    # Clear all session data from session directory.
    flask.session.clear()

    # If user reached login route via POST (e.g. submitting a POST form)
    if flask.request.method == "POST":
        # Ensure username was submitted.
        form_username = flask.request.form.get("username")
        if not form_username:
            return helpers.apology("must provide username", 403)

        # Ensure password was submitted.
        form_password = flask.request.form.get("password")
        if not form_password:
            return helpers.apology("must provide password", 403)

        # Query finance.db database for username.
        rows = db.execute("SELECT * FROM users WHERE username = ?", form_username)

        # Ensure username exists in database query and password is correct.
        if len(rows) != 1 or not werkzeug.security.check_password_hash(
            rows[0]["hash"], form_password
        ):
            return helpers.apology("invalid username and/or password", 403)

        # Assign user's finance.db id to their current session user_id.
        flask.session["user_id"] = rows[0]["id"]

        # Redirect the user to the homepage.
        return flask.redirect("/")

    # If user reached login route via GET (e.g. clicking link; redirect)
    else:
        return flask.render_template("login.html")


@app.route("/logout")
def logout() -> flask.Response:
    """Log user out."""

    # Clear all session data from session directory.
    flask.session.clear()

    # Redirect user to the login form.
    return flask.redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@helpers.login_required
def quote() -> flask.Response:
    """Look up stock's current price per user request."""

    # If user arrived to /quote via POST,
    if flask.request.method == "POST":
        # Verify that symbol form has input.
        form_symbol = flask.request.form.get("symbol")
        if not form_symbol:
            return helpers.apology("Missing symbol.")

        # Verify that symbol exists.
        symbol_data = helpers.lookup(form_symbol)
        if not symbol_data:
            return helpers.apology("Invalid symbol.")

        # Get data from lookup() return.
        name = symbol_data["name"]
        symbol = symbol_data["symbol"]

        # Format price with usd().
        fprice = helpers.usd(symbol_data["price"])

        # Render result template embedded with values from lookup().
        return flask.render_template("quoted.html",
                                     name=name, symbol=symbol, fprice=fprice)

    # If user arrived to /quote via GET, render quote form.
    else:
        return flask.render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register() -> flask.Response:
    """Register user into finance.db database via a form."""

    # If user navs to /register via POST (e.g. through form submission)
    if flask.request.method == "POST":
        # Retrieve user data from database.
        users = db.execute("SELECT * FROM users")

        # Apologize if no username was entered.
        form_username = flask.request.form.get("username")
        if not form_username:
            return helpers.apology("Must enter a username.")

        # Apologize if username already exists.
        username_exists = False
        for user in users:
            if user["username"] == form_username:
                username_exists = True
        if username_exists == True:
            return helpers.apology("Username already exists.")

        # Apologize if username has forbidden characters or length.
        if (re.search("[^a-zA-Z0-9_-]", form_username) or
            not 3 <= len(form_username) <= 16):
            return helpers.apology(
                "Username must only contain alphanumeric characters/"
                "underscores/hyphens and have a length of 3-16 characters."
            )

        # Apologize if no password was entered.
        form_password = flask.request.form.get("password")
        form_password_confirm = flask.request.form.get("password-confirm")
        if not form_password or not form_password_confirm:
            return helpers.apology(
                "Must enter a password and password confirmation."
            )

        # Apologize if passwords do not match.
        if form_password != form_password_confirm:
            return helpers.apology("Passwords do not match.")

        # Apologize if password is incorrect length.
        if not 8 <= len(form_password) <= 20:
            return helpers.apology(
                "Password must have a length of 8-20 characters."
            )


        # Initialize list of dicts for password requirements.
        password_reqs = [
            {
                "id": "lower",
                "check": "[a-z]",
                "met": True,
                "message": "Password does not contain lowercase character."
                },
            {
                "id": "upper",
                "check": "[A-Z]",
                "met": True,
                "message": "Password does not contain uppercase character."
            },
            {
                "id": "numeral",
                "check": "\d",
                "met": True,
                "message": "Password does not contain numeral 0-9."
            },
            {
                "id": "special",
                "check": "\W",
                "met": True,
                "message": "Password does not contain special character."
            },
            {
                "id": "no_username",
                "check": form_username,
                "met": True,
                "message": "Password contains username."
            },
        ]

        # Check if password fails to match requirements.
        valid_password = True
        for req in password_reqs:
            # Mark password invalid if requisite char is not found.
            if not re.search(rf"{req['check']}", form_password):
                if req["id"] != "no_username":
                    req["met"] = False
                    valid_password = False

            # Mark password invalid if username is found.
            else:
                if req["id"] == "no_username":
                    req["met"] = False
                    valid_password = False

        # If password fails to match reqs, apologize with specific error.
        if not valid_password:
            invalid_pw_message = "Password contained the following errors:"
            for req in password_reqs:
                if not req["met"]:
                    invalid_pw_message += f"\n{req['message']}"
            return helpers.apology(invalid_pw_message)

        # Hash password and clear reference to form_password variable data.
        hashed_form_password = (
            werkzeug.security.generate_password_hash(form_password)
        )
        form_password = None

        # Save new user into database; let id autoincrement in database.
        db.execute("INSERT INTO users (username, hash) "
                   "VALUES (?, ?)", form_username, hashed_form_password)

        # Query database for user id.
        new_user = db.execute("SELECT * FROM users "
                              "WHERE username = ?", form_username)

        # After successful registration, log user in and redirect home.
        if new_user:
            flask.session["user_id"] = new_user[0]["id"]
            return flask.redirect("/")

        # If new user does not exist, apologize for unknown error.
        else:
            return helpers.apology("Unknown error occurred.")

    # Render page if user did not arrive via POST.
    return flask.render_template("/register.html")


@app.route("/sell", methods=["GET", "POST"])
@helpers.login_required
def sell() -> flask.Response:
    """Sell shares of stock."""

    """Complete the implementation of sell in such a way that it enables a user to sell shares of a stock (that he or she owns).

    Require that a user input a stock’s symbol, implemented as a select menu whose name is symbol. Render an apology if the user fails to select a stock or if (somehow, once submitted) the user does not own any shares of that stock.
    Require that a user input a number of shares, implemented as a text field whose name is shares. Render an apology if the input is not a positive integer or if the user does not own that many shares of the stock.
    Submit the user’s input via POST to /sell.
    Upon completion, redirect the user to the home page.
    You don’t need to worry about race conditions (or use transactions).
    """








    return helpers.apology("TODO")
