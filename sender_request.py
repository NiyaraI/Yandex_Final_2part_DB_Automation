# Выполнить запрос на создание заказа.
# Сохранить номер трека заказа.
# Выполнить запрос на получения заказа по треку заказа.
# Проверить, что код ответа равен 200.

import requests
import config
import data

def get_order_track():
    responce = requests.post(config.stand_url + config.post_order, json=data.order_body)
    return responce.json()['track']

track = get_order_track()
print("track is", track)

def get_order_id(tr):
    responce = requests.get(config.stand_url + config.get_order_id_from_track+ "?t=" + str(tr))
    return responce.json()['order']['id']

get_id = get_order_id(track)
print("id is", get_id)

