"""

"""

from datetime import datetime
from flask import Flask, render_template

# Initiate instance of Flask class, conventionally named "app".
app = Flask(__name__)

# Display current date/time on homepage.
@app.route("/")
def time():
    time = datetime.now()
    return render_template("index.html", time=time)
