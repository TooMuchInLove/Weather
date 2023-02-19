# -*- coding: utf-8 -*-

# Аннотация типов
from typing import NamedTuple
# Структура данных для перечисления
from enum import Enum
# Дата и время
from datetime import datetime

# Локальный модули
from weather_gps import Coordinates

# ============================================= #
# ======= Подсказка типов Type Hinting ======== #
# ============================================= #
# Температура цельсий
Celsius = int


# Тип погоды
class WeatherType(Enum):
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDY = "Облачно"
    RAIN = "Дождь"
    THUNDERSTORM = "Гроза"
    FROST = "Изморозь"
    SNOW = "Снег"


# Данные погоды (Именованный кортеж)
class Weather(NamedTuple):
    # температура (цельсий)
    temperature: Celsius
    # тип погоды (облачно, дождь и т.д)
    weather_type: WeatherType
    # дата и время восхода
    sunrise: datetime
    # дата и время заката
    sunset: datetime


def get_weather(_coordinates: Coordinates) -> Weather:
    # Получаем широту и долготу
    latitude, longitude = _coordinates
    # Возвращаемое значение :params: данные погоды
    return Weather(
        temperature=4,
        weather_type=WeatherType.SNOW,
        sunrise=datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        sunset=datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    )
