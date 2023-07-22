"""

"""


import os

import cs50
import flask
"""
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
"""


MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


# Configure application
app = flask.Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = cs50.SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":

        # TODO: Add the user's entry into the database
        name = flask.request.form.get("name")
        if not flask.request.form.get("name"):
            flask.redirect("/")

        month = flask.request.form.get("month")
        if not flask.request.form.get("month"):
            flask.redirect("/")

        day = flask.request.form.get("day")
        if not flask.request.form.get("day"):
            flask.redirect("/")

        return flask.redirect("/")

    else:
        db.execute("SELECT * FROM birthdays;")
        return flask.render_template("index.html", months=MONTHS)

