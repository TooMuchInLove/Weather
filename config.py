# -*- coding: utf-8 -*-


# Хранилище локаций (страна + город)
LOCATION_STORAGE = {
    "Россия": (
        "Москва",
        "Санкт-Петербург",
        "Мурино",
        "Рыбинск",
        "Ярославль",
    ),
    "Russian": (
        "Moscow",
        "Saint-Petersburg",
        "Murino",
        "Rybinsk"
        "Yaroslavl",
    ),
    "Нидерланды": (
        "Амстердам",
    ),
    "Германия": (
        "Берлин",
    ),
    "Ирландия": (
        "Дублин",
    ),
    "Великобритания": (
        "Лондон",
    ),
}

# My secret key (OpenWeather)
OPENWEATHER_API = "39ef5ab9b17a34d049087a678398ea89"

# Url-address (OpenWeather)
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat=%s&lon=%s&appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)
