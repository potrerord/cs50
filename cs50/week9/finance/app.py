import os

import cs50
import flask
import flask_session
import tempfile
import werkzeug.security

import helpers

"""
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
"""

# Configure application
app = flask.Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = helpers.usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
flask_session.Session(app)

# Configure CS50 Library to use SQLite database
db = cs50.SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@helpers.login_required
def index():
    """Show portfolio of stocks"""
    return helpers.apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@helpers.login_required
def buy():
    """Buy shares of stock"""
    return helpers.apology("TODO")


@app.route("/history")
@helpers.login_required
def history():
    """Show history of transactions"""
    return helpers.apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    flask.session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if flask.request.method == "POST":

        # Ensure username was submitted
        if not flask.request.form.get("username"):
            return helpers.apology("must provide username", 403)

        # Ensure password was submitted
        elif not flask.request.form.get("password"):
            return helpers.apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", flask.request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not werkzeug.security.check_password_hash(rows[0]["hash"], flask.request.form.get("password")):
            return helpers.apology("invalid username and/or password", 403)

        # Remember which user has logged in
        flask.session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return flask.redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return flask.render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    flask.session.clear()

    # Redirect user to login form
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
