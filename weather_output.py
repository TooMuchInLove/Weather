# -*- coding: utf-8 -*-


def output_weather(_weather_data: tuple):
    # Данные для вывода
    data = _weather_data
    print("""
        Страна: %s
        Город: %s
        Широта: %s
        Долгота: %s
    """ % (data[0], data[1], data[2], data[3]))
