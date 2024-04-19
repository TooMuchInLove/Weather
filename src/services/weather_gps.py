# OpenStreetMap Nominatim API для получения широты и долготы из физического адреса
from geopy.geocoders import Nominatim
from src.containers import Coordinates
from src.config import LOCATION_STORAGE, LANGUAGE
from src.exc import (ErrorCountryDoesNotExist, ErrorCityDoesNotExist,
                     ErrorCantGetCoordinates, ErrorGeocoderService,
                     GeocoderServiceError,)


def get_gps_coordinates(country: str, city: str) -> Coordinates:
    """ Получение координат """
    latitude, longitude = _get_nominatim_coordinates(country, city)
    # Возвращаемое значение: широта & долгота
    return Coordinates(
        latitude=latitude,
        longitude=longitude
    )


def _get_nominatim_coordinates(country: str, city: str) -> Coordinates:
    """ Получаем координаты по местоположению с помощью Nominatim """
    _is_define_the_country_and_city(country, city)
    try:
        data = _get_nominatim()
        # Получаем словарь данных по местоположению
        data_list = data.geocode(f"{country}, {city}")
    except GeocoderServiceError:
        raise ErrorGeocoderService
    # Если данных нет (так как НЕкорректная страна/город)
    if data_list is not None:
        data_list = data_list.raw
    else:
        raise ErrorCantGetCoordinates
    # Возвращаемое значение - широта & долгота
    return Coordinates(
        latitude=data_list["lat"],
        longitude=data_list["lon"]
    )


def _is_define_the_country_and_city(country: str, city: str) -> None:
    """ Определяем, существует ли страна и город """
    # Если страна существует, то получаем список городов по ключу=страна
    city_items = LOCATION_STORAGE[LANGUAGE].get(country)
    if city_items is None:
        raise ErrorCountryDoesNotExist
    # Если город существует, то выбираем нужный ключ=город
    if city in city_items:
        return city_items[city_items.index(city)]
    else:
        raise ErrorCityDoesNotExist


def _get_nominatim() -> Nominatim:
    """ Возвращаем некоторые данные локации с помощью Nominatim """
    return Nominatim(user_agent="tutorial")
