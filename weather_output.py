# -*- coding: utf-8 -*-


def output_weather(_weather_types: dict):
    # Данные для вывода
    weather_types = _weather_types
    print("""
    %s
    %s, %s
        %s°C
    %s, %s
    |   Влажность: %s%%
    |   Скорость ветра: %s м/с
    |   Восход: %s
    |   Закат: %s
    """ % (
        weather_types["date_now"],
        weather_types["country"],
        weather_types["city"],
        weather_types["temperature"],

        weather_types["type"],
        weather_types["description"],
        weather_types["humidity"],
        weather_types["wind_speed"],

        weather_types["sunrise"],
        weather_types["sunset"],
    ))
