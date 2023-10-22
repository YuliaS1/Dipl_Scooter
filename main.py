# Серенко Юлия, 9-я когорта — Финальный проект. Инженер по тестированию плюс

from create_orders_check_track import save_track_number, get_info_order_by_track_number


def test_check_response_200():
    track = save_track_number()
    get_info_order_by_track_number(track)