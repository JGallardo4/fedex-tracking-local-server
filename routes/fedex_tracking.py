from flask import Blueprint, request, make_response, jsonify
from utils.fedex_utils  import get_delivery_date

fedex_tracking = Blueprint('/api/fedex-tracking', __name__)

@fedex_tracking.route("/api/fedex-tracking", methods=["GET"])
def get_delivery_date():
    print(request.args)
    return "", 200

    # tracking_number = request.args["trackingNumber"]

    # date = None

    # try:
    #     date = utils.get_delivery_date(tracking_number)
    # except Exception as e:
    #     print(e)

    # return make_response(jsonify(date), 200)