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

def output_weather_colors(_weather: Weather) -> str:
    return """
    \033[31m%s\033[0m
    %s
        \033[36m %s°C \033[0m
    %s, %s
    \033[31m|\033[0m   Влажность: \033[34m%s%%\033[0m
    \033[31m|\033[0m   Скорость ветра: \033[34m%s\033[0m м/с
    \033[31m|\033[0m   Восход: \033[34m%s\033[0m
    \033[31m|\033[0m   Закат: \033[34m%s\033[0m
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
