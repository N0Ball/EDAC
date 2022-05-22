from flask import Flask

from .routes.parity import Parity
from .routes.hammingcode import HammingCode

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World"

app.register_blueprint(Parity().get_route(), url_prefix='/parity')
app.register_blueprint(HammingCode().get_route(), url_prefix='/hammingCode')

if __name__ == '__main__':
    app.run()