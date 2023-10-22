import requests

import configuration
import data


# Выполнить запрос на создание заказа.
def create_new_order():
    new_order_responce = requests.post(configuration.BASE_URL + configuration.CREATE_ORDER,
                                       json=data.create_order_body)
    return new_order_responce


# Сохранить номер трека заказа.
def save_track_number():
    track_number = create_new_order().json()['track']
    return track_number


# Выполнить запрос на получения заказа по треку заказа.
def get_info_order_by_track_number(track_number):
    result_responce = requests.get(configuration.BASE_URL + configuration.GET_INFO_TRACK + str(track_number))
    assert result_responce.status_code == 200
    return result_responce


# Проверить, что код ответа равен 200.
def test_check_response_200():
    track = save_track_number()
    get_info_order_by_track_number(track)

