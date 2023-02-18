#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

# Локальный модули
from weather_gps import set_location
from weather_gps import get_gps_coordinates
from weather_output import data_output


# ===== ПОГОДА =============== #
def weather():
    # ===== Структура приложения =============== #
    # Страна, город
    country, city = "Россия", "Ярославль"

    set_location(country, city)
    print("Страна: %s\nГород: %s" % (country, city))

    coordinates = get_gps_coordinates()
    #print(coordinates)
    print("Широта: %s\nДолгота: %s" % (coordinates.latitude, coordinates.longitude))

    weather_data = (
        country,
        city,
        coordinates.latitude,
        coordinates.longitude,
    )

    print(data_output())


def main():
    weather()


if __name__ == "__main__":
    main()
