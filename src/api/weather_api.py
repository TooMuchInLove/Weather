from datetime import datetime
from ssl import _create_unverified_context as ssl_create_unverified_context
from json import loads
from urllib.request import urlopen
from src.containers import Coordinates, WeatherType, Weather
from src.config import OPENWEATHER_URL
from src.exc import URLError, ErrorApiService


def get_weather(coordinates: Coordinates, country: str, city: str) -> Weather:
    # Конвертируем объект в формат json
    open_weather = loads(_parse_openweather(coordinates))
    # Возвращаемое значение: данные о погоде
    return Weather(
        date_now=_get_datetime_now(),
        place=_get_place(country, city),
        temperature=_parse_openweather_temperature(open_weather),
        humidity=_parse_openweather_humidity(open_weather),
        wind_speed=_parse_openweather_wind(open_weather),
        weather_type=_parse_openweather_type(open_weather),
        description=_parse_openweather_description(open_weather),
        sunrise=_parse_openweather_datetime(open_weather, "sunrise"),
        sunset=_parse_openweather_datetime(open_weather, "sunset"),
    )


def _parse_openweather(coordinates: Coordinates):
    # Получаем широту и долготу
    latitude, longitude = coordinates
    # Доступ к средствам шифрования безопасности (ssl "Secure Sockets Layer")
    _create_default_https_context = ssl_create_unverified_context
    # Формируем URL для сайта OpenWeather
    url = OPENWEATHER_URL % (latitude, longitude)
    try:  # Парсим сайт OpenWeather и получаем некоторый объект
        return urlopen(url).read()
    except URLError:
        raise ErrorApiService


def _get_datetime_now() -> str:
    return datetime.now().strftime("%d %B, %Y %H:%M:%S")


def _get_place(country: str, city: str) -> str:
    return f"{country}, {city}"


def _parse_openweather_temperature(openweather: dict) -> int:
    try:
        return int(openweather["main"]["temp"])
    except (KeyError, TypeError):
        raise ErrorApiService


def _parse_openweather_humidity(openweather: dict) -> int:
    try:
        return int(openweather["main"]["humidity"])
    except (KeyError, TypeError):
        raise ErrorApiService


def _parse_openweather_wind(openweather: dict) -> float:
    try:
        return float(openweather["wind"]["speed"])
    except (KeyError, TypeError):
        raise ErrorApiService


def _parse_openweather_type(openweather: dict) -> str:
    try:  # идентификатор погоды
        weather_id = str(openweather["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ErrorApiService
    # Состояние погоды
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.FROST,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "8": WeatherType.CLOUDY,
        "800": WeatherType.CLEAR,
    }
    for key, item in weather_types.items():
        if weather_id.startswith(key):
            return item.value
    else:
        raise ErrorApiService


def _parse_openweather_description(openweather: dict) -> str:
    try:
        return openweather["weather"][0]["description"]
    except (KeyError, TypeError):
        raise ErrorApiService


def _parse_openweather_datetime(openweather: dict, type: str) -> str:
    try:
        return datetime.fromtimestamp(openweather["sys"][type]).strftime("%H:%M")
    except (KeyError, TypeError):
        raise ErrorApiService
