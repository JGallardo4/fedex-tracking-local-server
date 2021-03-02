import logging
import sys

from ..config import CONFIG_OBJ
from fedex.services.track_service import FedexTrackRequest

def get_delivery_date(tracking_number):
    customer_transaction_id = "*** TrackService Request v10 using Python ***"  # Optional transaction_id
    track = FedexTrackRequest(CONFIG_OBJ, customer_transaction_id=customer_transaction_id)

    # Track by Tracking Number
    track.SelectionDetails.PackageIdentifier.Type = 'TRACKING_NUMBER_OR_DOORTAG'
    track.SelectionDetails.PackageIdentifier.Value = tracking_number

    del track.SelectionDetails.OperatingCompany

    track.send_request()
    
    for match in track.response.CompletedTrackDetails[0].TrackDetails:
        event_details = []    
        if hasattr(match, 'Events'):
            for j in range(len(match.Events)):
                event_match = match.Events[j]
                event_details.append({'created': event_match.Timestamp, 'type': event_match.EventType,
                                    'description': event_match.EventDescription})

                if hasattr(event_match, 'StatusExceptionDescription'):
                    event_details[j]['exception_description'] = event_match.StatusExceptionDescription

    delivery_date = None

    for item in event_details:
        if item["description"] == "Delivered":
            delivery_date = item["created"].strftime("%b %d, %Y")
    
    return delivery_date
