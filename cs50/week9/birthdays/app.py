"""

"""


import os

import cs50
import flask
"""
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
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

        # TODO: Add the user's entry into the database

        return flask.redirect("/")

    else:

        # TODO: Display the entries in the database on index.html

        return flask.render_template("index.html")


