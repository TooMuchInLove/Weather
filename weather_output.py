# -*- coding: utf-8 -*-

# Локальный модули
from weather_api_service import Weather


def output_weather(_weather: Weather) -> str:
    return """
    %s
    %s
        %s°C
    %s, %s
    |   Влажность: %s%%
    |   Скорость ветра: %s м/с
    |   Восход: %s
    |   Закат: %s
    """ % (
        _weather.date_now,
        _weather.place,
        _weather.temperature,
        _weather.weather_type,
        _weather.description,
        _weather.humidity,
        _weather.wind_speed,
        _weather.sunrise,
        _weather.sunset
    )
