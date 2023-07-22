"""

"""

from datetime import datetime
from flask import Flask, render_template

# Initiate instance of Flask class, conventionally named "app".
app = Flask(__name__)

#
@app.route("/")
def get_time():
    current_time = datetime.now()
    return render_template("index.html", now=current_time)
