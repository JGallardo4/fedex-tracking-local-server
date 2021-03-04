from flask import Flask
from flask_cors import CORS

from routes.fedex_tracking import fedex_tracking

app = Flask(__name__)
CORS(app)

app.register_blueprint(fedex_tracking)

if  __name__ == "__main__":
    app.run()