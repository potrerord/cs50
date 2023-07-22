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
"""
First, in app.py, add logic in your GET request handling to query the birthdays.db database for all birthdays. Pass all of that data to your index.html template.
Then, in index.html, add logic to render each birthday as a row in the table. Each row should have two columns: one column for the person’s name and another column for the person’s birthday.
When the / route is requested via POST, your web application should add a new birthday to your database and then re-render the index page.
First, in index.html, add an HTML form. The form should let users type in a name, a birthday month, and a birthday day. Be sure the form submits to / (its “action”) with a method of post.
Then, in app.py, add logic in your POST request handling to INSERT a new row into the birthdays table based on the data supplied by the user.
Optionally, you may also:

Add the ability to delete and/or edit birthday entries.
Add any additional features of your choosing!


"""

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
        # Retrieve data from user's form fill.
        name = flask.request.form.get("name")
        month = flask.request.form.get("month")
        day = flask.request.form.get("day")

        # If any part of the form is empty, return failure page.
        if not name or not month or not day:
            return flask.render_template("failure.html")

        # If month or day is an invalid value, return failure page.
        elif not 1 <= month <= 12 or not 1 <= day <= 31:
            return flask.render_template("failure.html")


        # If all fields are present, update database and redirect home.
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        return flask.redirect("/")

    else:
        # When the / route is requested via GET, your web application
        # should display, in a table, all of the people in your database
        # along with their birthdays.
        birthdays = db.execute("SELECT * FROM birthdays")
        return flask.render_template("index.html", birthdays=birthdays)

