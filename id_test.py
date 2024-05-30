import requests
import config
import data
import sender_request

def test_get_order_id():
    track = sender_request.get_order_track()
    response = requests.get(config.stand_url + config.get_order_id_from_track + "?t=" + str(track))

    assert response.status_code == 200

