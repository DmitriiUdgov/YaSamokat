import configuration
import requests
import data


def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

def get_info_order(track):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track}"
    response = requests.get(get_order_url)
    return response