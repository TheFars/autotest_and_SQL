# Максим Шляхов, 20-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


# Функция для получения трекера заказа
def get_track(order_response):
    return order_response.json().get("track")



# Автотест
def test_order():
    post_order = sender_stand_request.post_new_order(data.order_body)  # Выполняем запрос на создание заказа
    data.track = get_track(post_order)  # Получаем и сохраняем номер трек заказа в data.track
    track_response = sender_stand_request.get_order(data.params_track)  # Выполняем запрос на получение заказа по треку
    assert track_response.status_code == 200  # Проверяем, что код ответа равен 200


