from flask import Blueprint, request, make_response, jsonify
from ..utils import utils

fedex = Blueprint('/api/fedex', __name__)

@fedex.route("/api/fedex", methods=["GET"])
def get_users():
    # data = request.get_json()
    # print(request)
    # tracking_number = data["tracking_number"]
    tracking_number = "921547187146"
    date = None
    try:
        date = utils.get_delivery_date(tracking_number)
    except Exception as e:
        print(e)

    return make_response(jsonify(date), 200)