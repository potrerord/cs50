"""

"""

from datetime import datetime
from flask import Flask, render_template, request

# Initiate instance of Flask class, conventionally named "app".
app = Flask(__name__)


@app.route("/")
def now():
    now = datetime.now()
    return render_template()
