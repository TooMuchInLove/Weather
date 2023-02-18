# -*- coding: utf-8 -*-

# Аннотация типов
from typing import Tuple, NamedTuple
# OpenStreetMap Nominatim API для получения широты и долготы из физического адреса
from geopy.geocoders import Nominatim

# Локальный config
from config import LOCATION_STORAGE

# ============================================= #
# ======= Подсказка типов Type Hinting ======== #
# ============================================= #
# Название страны
COUNTRY = str
# Название города
CITY = str
# Название локации (страна + город)
LOCATION = Tuple[COUNTRY, CITY]


# ============================================= #
# ======= Глобальный переменные =============== #
# ============================================= #
# Название страны
NAME_COUNTRY = str
# Название города
NAME_CITY = str


# Координаты (широта + долгота)
class Coordinates(NamedTuple):
    latitude: float
    longitude: float


# Устанавливаем локацию (страна + город)
def set_location(_country: COUNTRY, _city: CITY):
    global NAME_COUNTRY
    global NAME_CITY
    NAME_COUNTRY = _country
    NAME_CITY = _city
    # Получаем кортеж городов по ключу (страна)
    country_item = LOCATION_STORAGE.get(NAME_COUNTRY)
    print(country_item)
    # Если название города существует (по ключу - страна)
    if NAME_CITY in country_item:
        position = country_item.index(NAME_CITY)
        NAME_CITY = country_item[position]
    # Если название города НЕсуществует (по ключу - страна)
    else:
        NAME_CITY = "Такого города нет"
        # ===== Будет исключение ===== #
        pass


# Получение координал по локации (страна + город)
# def get_gps_coordinates(_country: COUNTRY, _city: CITY) -> Coordinates:
def get_gps_coordinates() -> Coordinates:
    global NAME_COUNTRY
    global NAME_CITY
    # Получаем данные по локации и прочее
    data = Nominatim(user_agent="tutorial")
    # Получаем словарь данных по местоположению
    location = data.geocode("%s, %s" % (NAME_COUNTRY, NAME_CITY)).raw
    # Возвращаемое значение :params: широта + долгота
    return Coordinates(latitude=location["lat"], longitude=location["lon"])


# from enum import Enum
#
# class GPSLocations(Enum):
#     US_RUSSIA = ("Russian", "sdlikg", "dg")
#     RU_RUSSIA = ("Россия",)
#
#
# for item in GPSLocations:
#     print(item.name, item.value[0])
