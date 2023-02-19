# -*- coding: utf-8 -*-

# Аннотация типов
from typing import NamedTuple
# Структура данных для перечисления
from enum import Enum
# Дата и время
from datetime import datetime
# Доступ к средствам шифрования безопасности (ssl "Secure Sockets Layer")
import ssl
# Преобразовываем данные в json
from json import loads
# Делаем запрос
import urllib.request
# Ошибка запроса
from urllib.error import URLError

# Локальный config
from config import OPENWEATHER_URL
# Локальный модули
from weather_gps import Coordinates, COUNTRY, CITY
# Локальный исключения
from exceptions import ErrorApiService

# ============================================= #
# ======= Подсказка типов Type Hinting ======== #
# ============================================= #
# Дата и время
DateTime = str
# Температура цельсий
Celsius = int
# Процент влажности
PercentageOfHumidity = int
# Скорость ветра
WindSpeed = float
# Место (страна и город)
PLACE = str


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
    # Дата и время сейчас
    date_now: DateTime
    # Место (страна и город)
    place: PLACE
    # температура (цельсий)
    temperature: Celsius
    # Процент влажности
    humidity: PercentageOfHumidity
    # Скорость ветра
    wind_speed: WindSpeed
    # тип погоды (облачно, дождь и т.д)
    weather_type: WeatherType
    # краткое описание погода
    description: str
    # дата и время восхода
    sunrise: DateTime
    # дата и время заката
    sunset: DateTime


def get_weather(_coordinates: Coordinates, _country: COUNTRY, _city: CITY) -> Weather:
    # Конвертируем объект в формат json
    open_weather = loads(_parse_openweather(_coordinates))
    # Возвращаемое значение :params: данные погоды
    return Weather(
        date_now=_parse_datetime_now(),
        place="%s, %s" % (_country, _city),
        temperature=_parse_openweather_temperature(open_weather),
        humidity=_parse_openweather_humidity(open_weather),
        wind_speed=_parse_openweather_wind(open_weather),
        weather_type=_parse_openweather_type(open_weather),
        description=_parse_openweather_description(open_weather),
        sunrise=_parse_openweather_datetime(open_weather, "sunrise"),
        sunset=_parse_openweather_datetime(open_weather, "sunset"),
    )


def _parse_openweather(_coordinates: Coordinates):
    # Получаем широту и долготу
    latitude, longitude = _coordinates
    # Доступ к средствам шифрования безопасности (ssl "Secure Sockets Layer")
    ssl._create_default_https_context = ssl._create_unverified_context
    # Формируем URL для сайта OpenWeather
    url = OPENWEATHER_URL % (latitude, longitude)
    try: # Парсим сайт OpenWeather и получаем некоторый объект
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ErrorApiService


def _parse_datetime_now() -> DateTime:
    return datetime.now().strftime("%d %B, %Y %H:%M:%S")


def _parse_openweather_datetime(_openweather: dict, _type: str) -> DateTime:
    return datetime.fromtimestamp(_openweather["sys"][_type]).strftime("%H:%M")


def _parse_openweather_temperature(_openweather: dict) -> Celsius:
    try:
        return int(_openweather["main"]["temp"])
    except TypeError:
        raise ErrorApiService


def _parse_openweather_humidity(_openweather: dict) -> PercentageOfHumidity:
    try:
        return int(_openweather["main"]["humidity"])
    except TypeError:
        raise ErrorApiService


def _parse_openweather_wind(_openweather: dict) -> WindSpeed:
    try:
        return float(_openweather["wind"]["speed"])
    except TypeError:
        raise ErrorApiService


def _parse_openweather_type(_openweather: dict) -> WeatherType:
    try: # идентификатор погода
        weather_id = str(_openweather["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ErrorApiService
    # Состояние погоды
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.FROST,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "8": WeatherType.CLOUDY
    }
    for key, item in weather_types.items():
        if weather_id.startswith(key):
            return item.value
    else:
        raise ErrorApiService


def _parse_openweather_description(_openweather: dict) -> str:
    try:
        return _openweather["weather"][0]["description"]
    except TypeError:
        raise ErrorApiService
