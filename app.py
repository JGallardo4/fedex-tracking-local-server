from flask import Flask
from flask_cors import CORS

from routes.track import track

app = Flask(__name__)
CORS(app)

app.register_blueprint(track)

if  __name__ == "__main__":
    app.run()