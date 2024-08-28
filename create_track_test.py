# Максим Шляхов, 20-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


# Функция для получения трекера заказа
def get_track(order_response):
    return order_response.json().get("track")


data.params_track["t"] = get_track(sender_stand_request.order_response)


# Автотест
def positive_assert():
    track_response = sender_stand_request.get_order(data.params_track)
    assert track_response.status_code == 200


def test_order():
    positive_assert()

