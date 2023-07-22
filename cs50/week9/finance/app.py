"""

"""


import os  # contains functions to interact with operating system

import cs50  # contains SQL setup
import flask  # micro web framework including tools/libraries/tech to build web apps with python
import flask_session  # allows you to store session data on server side
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

# Configure CS50 Library's SQL module to use SQLite finance.db database.
db = cs50.SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached."""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@helpers.login_required
def index():
    """Show portfolio of stocks."""









    return helpers.apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@helpers.login_required
def buy():
    """Buy shares of stock."""











    return helpers.apology("TODO")


@app.route("/history")
@helpers.login_required
def history():
    """Show history of transactions."""













    return helpers.apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
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
        if len(rows) != 1 or not werkzeug.security.check_password_hash(rows[0]["hash"], form_password):
            return helpers.apology("invalid username and/or password", 403)

        # Assign user's finance.db id to their current session user_id.
        flask.session["user_id"] = rows[0]["id"]

        # Redirect the user to the homepage.
        return flask.redirect("/")

    # If user reached login route via GET (e.g. clicking link; redirect)
    else:
        return flask.render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out."""

    # Clear all session data from session directory.
    flask.session.clear()

    # Redirect user to the login form.
    return flask.redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@helpers.login_required
def quote():
    """Get stock quote."""
    return helpers.apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    return helpers.apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@helpers.login_required
def sell():
    """Sell shares of stock"""
    return helpers.apology("TODO")
