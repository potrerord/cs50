"""

"""


import os

import cs50
import flask
"""
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
"""

MONTH_DAYS = {
     '1': 31,
     '2': 29,
     '3': 31,
     '4': 30,
     '5': 31,
     '6': 30,
     '7': 31,
     '8': 31,
     '9': 30,
    '10': 31,
    '11': 31,
    '12': 31
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
        user_name = flask.request.form.get("name")
        user_month = flask.request.form.get("month")
        user_day = flask.request.form.get("day")

        # If any part of the form is empty, render failure page.
        if not user_name or not user_month or not user_day:
            return flask.render_template("failure.html")

        # If invalid date, render failure page.
        elif not 1 <= int(user_month) <= 12 or not 1 <= int(user_day) <= MONTH_DAYS[user_month]:
            return flask.render_template("failure.html")

        # If all fields are valid, update database and redirect home.
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", user_name, user_month, user_day)
        return flask.redirect("/")

    else:
        # Query for all birthdays.
        birthdays = db.execute("SELECT * FROM birthdays")
        print(f"\n{birthdays}\n")

        # Render birthdays page.
        return flask.render_template("index.html", birthdays=birthdays)

