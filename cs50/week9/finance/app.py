"""

"""


import os  # contains functions to interact with operating system

import cs50  # contains SQL setup
import flask  # micro web framework including tools/libraries/tech to build web apps with python
import flask_session  # allows you to store session data on server side
import re
import tempfile  # python standard library module to create temporary files during exec
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

    """Complete the implementation of index in such a way that it displays an HTML table summarizing, for the user currently logged in, which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding (i.e., shares times price). Also display the user’s current cash balance along with a grand total (i.e., stocks’ total value plus cash).

    Odds are you’ll want to execute multiple SELECTs. Depending on how you implement your table(s), you might find GROUP BY HAVING SUM and/or WHERE of interest.
    Odds are you’ll want to call lookup for each stock.
    """







    return helpers.apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@helpers.login_required
def buy() -> flask.Response:
    """Buy shares of stock."""

    """Complete the implementation of buy in such a way that it enables a user to buy stocks.

    Require that a user input a stock’s symbol, implemented as a text field whose name is symbol. Render an apology if the input is blank or the symbol does not exist (as per the return value of lookup).
    Require that a user input a number of shares, implemented as a text field whose name is shares. Render an apology if the input is not a positive integer.
    Submit the user’s input via POST to /buy.
    Upon completion, redirect the user to the home page.
    Odds are you’ll want to call lookup to look up a stock’s current price.
    Odds are you’ll want to SELECT how much cash the user currently has in users.
    Add one or more new tables to finance.db via which to keep track of the purchase. Store enough information so that you know who bought what at what price and when.
    Use appropriate SQLite types.
    Define UNIQUE indexes on any fields that should be unique.
    Define (non-UNIQUE) indexes on any fields via which you will search (as via SELECT with WHERE).
    Render an apology, without completing a purchase, if the user cannot afford the number of shares at the current price.
    You don’t need to worry about race conditions (or use transactions).
    Once you’ve implemented buy correctly, you should be able to see users’ purchases in your new table(s) via phpLiteAdmin or sqlite3.

    """









    return helpers.apology("TODO")


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
    """Get stock quote."""

    """Complete the implementation of quote in such a way that it allows a user to look up a stock’s current price.

    Require that a user input a stock’s symbol, implemented as a text field whose name is symbol.
    Submit the user’s input via POST to /quote.
    Odds are you’ll want to create two new templates (e.g., quote.html and quoted.html). When a user visits /quote via GET, render one of those templates, inside of which should be an HTML form that submits to /quote via POST. In response to a POST, quote can render that second template, embedding within it one or more values from lookup.
    """








    return helpers.apology("TODO")


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

        # Apologize if no password was entered.
        form_password = flask.request.form.get("password")
        form_password_confirm = flask.request.form.get("password-confirm")
        if not form_password or not form_password_confirm:
            return helpers.apology("Must enter a password and password confirmation.")

        # Apologize if passwords do not match.
        if form_password != form_password_confirm:
            return helpers.apology("Passwords do not match.")

        # Check if password fails to match requirements.
        invalid = [
            {"no_lower": False, 
            no_upper: [False
            no_num: [False
            no_spec: [False
            contains_user: [False
        ]
        if not re.search(r"[a-z]", form_password):
            no_lower = True
        elif not re.search(r"[A-Z]", form_password):
            no_upper = True
        elif not re.search(r"\d", form_password):
            no_num = True
        elif not re.search(r"\W", form_password):
            no_spec = True
        elif re.search(form_username, form_password):
            contains_user = True

        # If password fails to match requirements, provide specified error.
        if no_lower or no_upper or no_num or no_spec or contains_user:




        # Hash password before saving it into database.
        hashed_form_password = werkzeug.security.generate_password_hash(form_password)

        # Save new user into database; let id autoincrement in database.
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", form_username, hashed_form_password)

        # Query database for user id.
        new_user = db.execute("SELECT * FROM users WHERE username = ?", form_username)

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
