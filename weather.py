#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

# Локальный модули
from weather_gps import set_location
from weather_gps import get_gps_coordinates
from weather_api_service import get_weather
from weather_output import output_weather
# Локальные исключения
from exceptions import ErrorCountryDoesNotExist
from exceptions import ErrorCityDoesNotExist
from exceptions import ErrorCantGetCoordinates


# Завершаем работу программы
def _exit_program():
    exit(1)


def weather():
    # Страна, город
    country, city = "Россия", "Москва"
    try:
        # Определяем местоположение
        set_location(country, city)
        # Определяем координаты
        coordinates = get_gps_coordinates()
        # Получаем данные о погоде
        # print(get_weather(coordinates))
        # Данные о погоде
        weather_data = (
            country,
            city,
            coordinates.latitude,
            coordinates.longitude,
        )
        output_weather(weather_data)
    except ErrorCountryDoesNotExist:
        _exit_program()
    except ErrorCityDoesNotExist:
        _exit_program()
    except ErrorCantGetCoordinates:
        _exit_program()


def main():
    weather()


if __name__ == "__main__":
    main()
