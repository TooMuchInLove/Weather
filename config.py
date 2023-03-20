# -*- coding: utf-8 -*-

# Ширина приложения
WIDTH = 330
# Высота приложения
HEIGHT = 320

# Логотип приложения
ICON_URL = "icon/weather.png"

# My secret key (OpenWeather)
OPENWEATHER_API = "39ef5ab9b17a34d049087a678398ea89"

# Url-address (OpenWeather)
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat=%s&lon=%s&appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)

# Хранилище локаций (страна + город)
LOCATION_STORAGE = {
    "Россия": (
        "Москва",
        "Санкт-Петербург",
        "Мурино",
        "Рыбинск",
        "Ярославль",
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
    # "Russian": (
    #     "Moscow",
    #     "Saint-Petersburg",
    #     "Murino",
    #     "Rybinsk"
    #     "Yaroslavl",
    # ),
}
