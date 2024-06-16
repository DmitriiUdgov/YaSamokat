import configuration
import requests
import data


# Создаем новый заказ
def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


order_track = new_order(data.order_body).json()["track"]


# Получаем данные о заказе по номеру
def get_info_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))