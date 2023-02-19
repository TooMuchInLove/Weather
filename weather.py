#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

# Определяем текущую директорию
from pathlib import Path

# Локальный модули
from weather_gps import set_location
from weather_gps import get_gps_coordinates
from weather_api_service import get_weather
from weather_output import output_weather
from logging_ import save_weather, TXTFileStorage
# Локальные исключения
from exceptions import ErrorCountryDoesNotExist
from exceptions import ErrorCityDoesNotExist
from exceptions import ErrorCantGetCoordinates
from exceptions import ErrorApiService


def main():
    # Страна, город
    country, city = "Нидерланды", "Амстердам"
    try:
        # Определяем местоположение
        set_location(country, city)
        # Определяем координаты
        coordinates = get_gps_coordinates()
        # Получаем данные о погоде
        weather_types = get_weather(coordinates, country, city)
        # Отображаем данные
        print(output_weather(weather_types))
        # Логгирование в текстовый документ
        save_weather(weather_types, TXTFileStorage(Path.cwd()/"logging.txt"))
    except ErrorCountryDoesNotExist:
        exit(1)
    except ErrorCityDoesNotExist:
        exit(1)
    except ErrorCantGetCoordinates:
        exit(1)
    except ErrorApiService:
        exit(1)


if __name__ == "__main__":
    main()
