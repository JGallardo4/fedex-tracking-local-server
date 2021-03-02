from flask import Flask

from ._routes.fedex import fedex

app = Flask(__name__)
app.register_blueprint(fedex)