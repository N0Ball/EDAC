from flask import Flask

from .view.parity import Parity
from .view.hammingcode import HammingCode

app = Flask(__name__)

app.run()

@app.route("/")
def home():
    return "Hello, World"

app.register_blueprint(Parity().get_route(), url_prefix='/parity')
app.register_blueprint(HammingCode().get_route(), url_prefix='/hammingCode')