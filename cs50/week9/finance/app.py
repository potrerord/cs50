"""
Runs Flask app for C$50.
"""


import os  # contains functions to interact with operating system
from datetime import datetime
from tempfile import mkdtemp  # create temporary files during exec
from typing import Dict, Union  # used in type hints

from cs50 import SQL  # contains SQL setup
import flask  # micro web framework to build web apps with python
from flask_session import Session  # store session data on server side
import re  # regex searches
import pytz  # timezone functionality
from werkzeug.security import check_password_hash, generate_password_hash

import helpers  # local file with helper functions


# Configure Flask application in current file.
app = flask.Flask(__name__)

# Configure Jinja environment with custom USD formatting filter.
app.jinja_env.filters["usd"] = helpers.usd

# Configure Flask to store sessions on local disk (not signed cookies).
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Create SQL class object from CS50 library with finance.db database.
db = SQL("sqlite:///finance.db")

# Create transaction history table if it does not already exist.
db.execute(
    """
    CREATE TABLE IF NOT EXISTS transactions (
        id           INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
        user_id      INTEGER  NOT NULL,
        type         TEXT     NOT NULL,
        symbol       TEXT     NOT NULL,
        shares       INTEGER  NOT NULL,
        shareprice   NUMERIC  NOT NULL,
        datetime_utc DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
)

# Create index on foreign key and datetime for searchability.
db.execute(
    """
    CREATE INDEX IF NOT EXISTS transactions_userid_idx
        ON transactions (user_id)
    """
)
db.execute(
    """
    CREATE INDEX IF NOT EXISTS transactions_datetimeutc_idx
        ON transactions (datetime_utc)
    """
)

# Create portfolios table if it does not already exist.
db.execute(
    """
    CREATE TABLE IF NOT EXISTS portfolios (
        user_id     INTEGER  NOT NULL,
        symbol      TEXT     NOT NULL,
        owned       INTEGER  NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        PRIMARY KEY (user_id, symbol)
    )
    """
)

# Create index on foreign key and symbol for searchability.
db.execute(
    """
    CREATE INDEX IF NOT EXISTS portfolios_userid_idx
        ON portfolios (user_id)
    """
)
db.execute(
    """
    CREATE INDEX IF NOT EXISTS portfolios_symbol_idx
        ON portfolios (symbol)
    """
)


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

    # Get user's current cash.
    cash = db.execute(
        """
        SELECT cash
          FROM users
         WHERE users.id = ?
        """,
        flask.session["user_id"],
    )

    # Initialize variable for total portfolio value starting with cash.
    portfolio_value = cash[0]["cash"]

    # Get current user's portfolio data.
    portfolio = db.execute(
        """
        SELECT symbol, owned
          FROM portfolios
         WHERE portfolios.user_id = ?
           AND owned > 0
        """,
        flask.session["user_id"],
    )

    # Iterate through all stocks in user's portfolio.
    for stock in portfolio:
        # Update portfolio for this stock's current price data.
        stock["price"] = helpers.lookup(stock["symbol"])["price"]
        stock["shares_value"] = stock["price"] * stock["owned"]

        # Add the total value of shares to the portfolio value.
        portfolio_value += stock["shares_value"]

        # After precise calc, round if necessary and format strings.
        stock["price"] = helpers.usd(round(stock["price"], 2))
        stock["shares_value"] = helpers.usd(round(stock["shares_value"], 2))

    # Get UTC datetime of quote lookup.
    quote_time = datetime.now(pytz.timezone("UTC"))

    # Round and format remaining variables.
    cash = helpers.usd(cash[0]["cash"])
    portfolio_value = helpers.usd(round(portfolio_value, 2))

    # Render index with relevant variables for Jinja templating.
    return flask.render_template(
        "index.html",
        portfolio=portfolio,
        cash=cash,
        portfolio_value=portfolio_value,
        quote_time=quote_time,
    )


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
        try:
            form_shares = int(form_shares)
        except ValueError:
            return helpers.apology("Enter valid integer.")
        if form_shares < 1:
            return helpers.apology("Not enough shares.")

        # Get data from lookup() return.
        symbol = symbol_data["symbol"]
        price = symbol_data["price"]

        # Calculate total transaction amount.
        trans_amount = price * form_shares

        # Get user's pre- and post-transaction cash balance.
        user_cash = db.execute(
            """
            SELECT cash
              FROM users
             WHERE users.id = ?
            """,
            flask.session["user_id"],
        )
        if not user_cash[0]["cash"]:
            return helpers.apology("Unknown error.")
        pre_trans_cash = user_cash[0]["cash"]

        # Determine if user can afford transaction.
        post_trans_cash = pre_trans_cash - trans_amount
        if post_trans_cash < 0:
            return helpers.apology("Insufficient funds.")

        # Execute transaction by updating table at current UTC datetime.
        db.execute(
            """
            INSERT INTO transactions (user_id, shares, type, shareprice,
                                      symbol, datetime_utc)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            flask.session["user_id"],
            form_shares,
            "buy",
            price,
            symbol,
            datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        )

        # Get user's current shares of this stock.
        current_shares = db.execute(
            """
            SELECT owned
              FROM portfolios AS p
             WHERE p.user_id = ?
               AND p.symbol = ?
            """,
            flask.session["user_id"],
            symbol,
        )

        # Convert from list of dicts to single value.
        if not current_shares:
            current_shares = 0
        else:
            current_shares = current_shares[0]["owned"]

        # Update user's portfolio.
        db.execute(
            """
            INSERT OR REPLACE INTO portfolios (user_id, symbol, owned)
            VALUES (?, ?, ?)
            """,
            flask.session["user_id"],
            symbol,
            current_shares + form_shares,
        )

        # Update user's cash balance.
        db.execute(
            """
            UPDATE users AS u
               SET cash = ?
             WHERE id = ?
            """,
            post_trans_cash,
            flask.session["user_id"],
        )

        # Redirect to homepage after successful transaction.
        return flask.redirect("/")

    # If user arrived to /buy via GET, render buy form.
    else:
        return flask.render_template("buy.html")


@app.route("/history")
@helpers.login_required
def history() -> flask.Response:
    """Show user's entire transaction history."""

    user_history = db.execute(
        """
        SELECT *
          FROM transactions
         WHERE user_id = ?
        """,
        flask.session["user_id"],
    )

    # Reformat data to display to user.
    for transaction in user_history:
        # Format sells as negative shares.
        if transaction["type"] == "sell":
            transaction["shares"] = transaction["shares"] * -1

        # Format stock price as USD.
        transaction["shareprice"] = helpers.usd(transaction["shareprice"])

    # Complete the implementation of history in such a way that it
    # displays an HTML table summarizing all of a user’s transactions
    # ever, listing row by row each and every buy and every sell.

    # For each row, make clear whether a stock was bought or sold and
    # include the stock’s symbol, the (purchase or sale) price, the
    # number of shares bought or sold, and the date and time at which
    # the transaction occurred.

    return flask.render_template("history.html", user_history=user_history)


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
        rows = db.execute(
            """
            SELECT *
              FROM users
             WHERE users.username = ?
            """,
            form_username,
        )

        # Ensure username exists in database and password is correct.
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], form_password):
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

        # Get UTC datetime of quote.
        quote_time = datetime.now(pytz.timezone("UTC"))

        # Get data from lookup() return.
        name = symbol_data["name"]
        symbol = symbol_data["symbol"]

        # Format price with usd().
        fprice = helpers.usd(symbol_data["price"])

        # Render result template embedded with values from lookup().
        return flask.render_template(
            "quoted.html",
            name=name,
            symbol=symbol,
            fprice=fprice,
            quote_time=quote_time,
        )

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
        if (
            re.search("[^a-zA-Z0-9_-]", form_username)
            or not 3 <= len(form_username) <= 16
        ):
            return helpers.apology(
                "Username must only contain alphanumeric characters/"
                "underscores/hyphens and have a length of 3-16 characters."
            )

        # Apologize if no password was entered.
        form_password = flask.request.form.get("password")
        form_password_confirm = flask.request.form.get("confirmation")
        if not form_password or not form_password_confirm:
            return helpers.apology("Must enter a password and password confirmation.")

        # Apologize if passwords do not match.
        if form_password != form_password_confirm:
            return helpers.apology("Passwords do not match.")

        # Apologize if password is incorrect length.
        if not 8 <= len(form_password) <= 20:
            return helpers.apology("Password must have a length of 8-20 characters.")

        # Initialize list of dicts for password requirements.
        password_reqs = [
            {
                "id": "lower",
                "check": "[a-z]",
                "met": True,
                "message": "Password does not contain lowercase character.",
            },
            {
                "id": "upper",
                "check": "[A-Z]",
                "met": True,
                "message": "Password does not contain uppercase character.",
            },
            {
                "id": "numeral",
                "check": "\d",
                "met": True,
                "message": "Password does not contain numeral 0-9.",
            },
            {
                "id": "special",
                "check": "\W",
                "met": True,
                "message": "Password does not contain special character.",
            },
            {
                "id": "no_username",
                "check": form_username,
                "met": True,
                "message": "Password contains username.",
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
        hashed_form_password = generate_password_hash(form_password)
        form_password = None

        # Save new user into database; let id autoincrement in database.
        db.execute(
            "INSERT INTO users (username, hash) " "VALUES (?, ?)",
            form_username,
            hashed_form_password,
        )

        # Query database for user id.
        new_user = db.execute(
            "SELECT * FROM users " "WHERE username = ?", form_username
        )

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
    """Sell shares of stock on behalf of user request."""

    # Require that a user input a number of shares, implemented as a
    # text field whose name is shares. Render an apology if the input is
    # not a positive integer or if the user does not own that many
    # shares of the stock.

    # If user arrived to /sell via POST,
    if flask.request.method == "POST":
        # Verify that symbol form has input.
        form_symbol = flask.request.form.get("symbol")
        if not form_symbol:
            return helpers.apology("Missing symbol.")
        form_symbol = form_symbol.upper()

        # Verify that symbol exists.
        symbol_data = helpers.lookup(form_symbol)
        if not symbol_data:
            return helpers.apology("Invalid symbol.")

        # Verify that user owns at least one share of stock.
        user_stocks = db.execute(
            """
            SELECT symbol
              FROM portfolios
             WHERE portfolios.user_id = ?
            """,
            flask.session["user_id"],
        )
        if not user_stocks or form_symbol not in user_stocks[0]["symbol"]:
            return helpers.apology("Must own shares to sell stock.")

        # Verify that shares has input.
        form_shares = flask.request.form.get("shares")
        if not form_shares:
            return helpers.apology("Missing shares.")

        # Verify that shares is positive integer.
        try:
            form_shares = int(form_shares)
        except ValueError:
            return helpers.apology("Enter valid integer.")
        if form_shares < 1:
            return helpers.apology("Sold shares must be positive.")

        # Verify that user has enough shares to sell.
        user_shares = db.execute(
            """
            SELECT owned
              FROM portfolios AS p
             WHERE p.user_id = ?
               AND p.symbol = ?
            """,
            flask.session["user_id"],
            form_symbol,
        )
        if form_shares > user_shares[0]["owned"]:
            return helpers.apology("Insufficient shares to sell.")

        # Get data from lookup() return.
        symbol = symbol_data["symbol"]
        price = symbol_data["price"]

        # Calculate total transaction amount.
        trans_amount = price * form_shares

        # Get user's pre- and post-transaction cash balance.
        user_cash = db.execute(
            """
            SELECT cash
              FROM users
             WHERE users.id = ?
            """,
            flask.session["user_id"],
        )
        if not user_cash[0]["cash"]:
            return helpers.apology("Unknown error.")
        pre_trans_cash = user_cash[0]["cash"]
        post_trans_cash = round(pre_trans_cash + trans_amount, 2)

        # Execute transaction by updating table at current datetime.
        db.execute(
            """
            INSERT INTO transactions (user_id, shares, type, shareprice,
                                      symbol, datetime_utc)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            flask.session["user_id"],
            form_shares,
            "sell",
            price,
            symbol,
            datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        )

        # Get user's current shares of this stock.
        current_shares = db.execute(
            """
            SELECT owned
              FROM portfolios AS p
             WHERE p.user_id = ?
               AND p.symbol = ?
            """,
            flask.session["user_id"],
            symbol,
        )

        # Convert from list of dicts to single value.
        if not current_shares:
            current_shares = 0
        else:
            current_shares = current_shares[0]["owned"]

        # Update user's portfolio.
        db.execute(
            """
            INSERT OR REPLACE INTO portfolios (user_id, symbol, owned)
            VALUES (?, ?, ?)
            """,
            flask.session["user_id"],
            symbol,
            current_shares - form_shares,
        )

        # Update user's cash balance.
        db.execute(
            """
            UPDATE users
               SET cash = ?
             WHERE id = ?
            """,
            post_trans_cash,
            flask.session["user_id"],
        )

        # Redirect to homepage after successful transaction.
        return flask.redirect("/")

    # If user arrived to /sell via GET, render sell form.
    else:
        # Get current user's portfolio data.
        portfolio = db.execute(
            """
            SELECT symbol
              FROM portfolios
             WHERE portfolios.user_id = ?
               AND owned > 0
            """,
            flask.session["user_id"],
        )

        return flask.render_template("sell.html", portfolio=portfolio)
