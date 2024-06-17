import sender_stand_request
import data

# Дмитрий Удгов, 17-я когорта — Финальный проект. Инженер по тестированию плюс

def test_ordercreate_trackcheck():
    response = sender_stand_request.new_order(data.order_body)

    track = response.json()["track"]
    print("Order number: ", track)

    order_response = sender_stand_request.get_info_order(track)

    assert order_response.status_code == 200, f"Code {order_response.status_code}"
    order = order_response.json()
    print("Order", order)