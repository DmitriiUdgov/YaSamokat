import sender_stand_request
import data

# Дмитрий Удгов, 17-я когорта — Финальный проект. Инженер по тестированию плюс
# Делаем запрос на создание заказа
def test_create_order():
    response = sender_stand_request.new_order(data.order_body)
# Проверяем, что он создается без ошибок (код 201)
    assert response.status_code == 201


# Сохраняем номер трека
def test_save_order_track():
    order_track = sender_stand_request.new_order(data.order_body).json()["track"]
    return order_track
    print("zakaz:", order_track)

# Получение заказа по треку
def test_take_order_by_orders_track():
    response = sender_stand_request.get_info_order(sender_stand_request.order_track)
    assert response.status_code == 200
