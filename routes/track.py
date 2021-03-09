from flask import Blueprint, request, make_response, jsonify
from utils  import fedex_utils
import config

track = Blueprint('/api/track', __name__)

@track.route("/api/track", methods=["GET"])
def get_delivery_date():   
    date = None

    try:
        api_key = request.args["apiKey"]
        tracking_number = request.args["trackingNumber"]
        print(config.api_key)
        if api_key == config.api_key:
            date = fedex_utils.get_delivery_date(tracking_number)
            return make_response(jsonify(date), 200)
    except Exception as e:
        print(e)
        return "", 500    