from dataclasses import dataclass
from enum import Enum


class WeatherType(Enum):
    """ Тип погоды """
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDY = "Облачно"
    RAIN = "Дождь"
    THUNDERSTORM = "Гроза"
    FROST = "Изморозь"
    SNOW = "Снег"


@dataclass(slots=True, frozen=True)
class Weather:
    """ Данные погоды (временный контейнер) """
    date_now: str  # Дата и время сейчас
    place: str  # Место (страна и город)
    temperature: int  # температура (цельсий)
    humidity: int  # Процент влажности
    wind_speed: float  # Скорость ветра
    weather_type: str  # тип погоды (облачно, дождь и т.д)
    description: str  # краткое описание погода
    sunrise: str  # дата и время восхода
    sunset: str  # дата и время заката
