# -*- coding: utf-8 -*-

# Аннотация типов
from typing import NamedTuple
# OpenStreetMap Nominatim API для получения широты и долготы из физического адреса
from geopy.geocoders import Nominatim

# Локальный config
from config import LOCATION_STORAGE
# Локальный исключения
from exceptions import ErrorCountryDoesNotExist
from exceptions import ErrorCityDoesNotExist
from exceptions import ErrorCantGetCoordinates

# ============================================= #
# ======= Подсказка типов Type Hinting ======== #
# ============================================= #
# Название страны
COUNTRY = str
# Название города
CITY = str
# Координаты широта и долгота (Именованный кортеж)
class Coordinates(NamedTuple):
    latitude: float
    longitude: float

# ============================================= #
# ======= Глобальный переменные =============== #
# ============================================= #
# Название страны
NAME_COUNTRY = str
# Название города
NAME_CITY = str
# Список городов по названию страны
CITY_ITEMS = tuple


# Устанавливаем локацию (страна + город)
def set_location(_country: COUNTRY, _city: CITY):
    # Определяем, существует ли страна
    _define_the_country(_country)
    # Определяем, существует ли город
    _define_the_city(_city)


# Определяем страну
def _define_the_country(_country: COUNTRY) -> None:
    global NAME_COUNTRY
    global CITY_ITEMS
    # Если страна существует, то получаем список городов по ключу (страна)
    if _country in LOCATION_STORAGE.keys():
        NAME_COUNTRY = _country
        CITY_ITEMS = LOCATION_STORAGE[_country]
    else:
        raise ErrorCountryDoesNotExist


# Определяем город
def _define_the_city(_city: CITY) -> None:
    global NAME_CITY
    global CITY_ITEMS
    # Если город существует, то выбираем нужный город
    if _city in CITY_ITEMS:
        index = CITY_ITEMS.index(_city)
        NAME_CITY = CITY_ITEMS[index]
    else:
        raise ErrorCityDoesNotExist


# Получение координат
def get_gps_coordinates() -> Coordinates:
    latitude, longitude = _get_nominatim_coordinates()
    # Возвращаемое значение :params: широта + долгота
    return Coordinates(
        latitude=latitude,
        longitude=longitude
    )


# Получаем некоторые данные с помощью Nominatim
def _get_nominatim() -> Nominatim:
    # Возвращаемое значение :params: данные по локации и прочее
    return Nominatim(user_agent="tutorial")


# Получаем координаты по местоположению с помощью Nominatim
def _get_nominatim_coordinates() -> Coordinates:
    global NAME_COUNTRY
    global NAME_CITY
    data = _get_nominatim()
    # Получаем словарь данных по местоположению
    data_list = data.geocode("%s, %s" % (NAME_COUNTRY, NAME_CITY))
    # Если данных нет (так как НЕкорректная страна/город)
    if data_list is not None:
        data_list = data_list.raw
    else:
        raise ErrorCantGetCoordinates
    # Возвращаемое значение :params: широта + долгота
    return Coordinates(
        latitude=data_list["lat"],
        longitude=data_list["lon"]
    )
