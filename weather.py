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
from exceptions import ErrorApiService


# Завершаем работу программы
def _exit_program():
    exit(1)


def weather():
    # Страна, город
    country, city = "Ирландия", "Дублин"
    try:
        # Определяем местоположение
        set_location(country, city)
        # Определяем координаты
        coordinates = get_gps_coordinates()
        # Получаем данные о погоде
        other_data = get_weather(coordinates)
        # Данные о погоде
        weather_types = {
            "date_now": other_data.date_now,
            "country": country,
            "city": city,
            "temperature": other_data.temperature,
            "humidity": other_data.humidity,
            "wind_speed": other_data.wind_speed,
            "type": other_data.weather_type,
            "description": other_data.description,
            "sunrise": other_data.sunrise,
            "sunset": other_data.sunset,
        }
        output_weather(weather_types)
    except ErrorCountryDoesNotExist:
        _exit_program()
    except ErrorCityDoesNotExist:
        _exit_program()
    except ErrorCantGetCoordinates:
        _exit_program()
    except ErrorApiService:
        _exit_program()


def main():
    weather()


if __name__ == "__main__":
    main()
