"""

"""

from datetime import datetime
from flask import Flask

# Initiate instance of Flask class, conventionally named "app".
app = Flask(__name__)


def now():
    return datetime.now()

@app.route("/")