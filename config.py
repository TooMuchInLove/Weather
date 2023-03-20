# -*- coding: utf-8 -*-

# Ширина приложения
WIDTH = 330
# Высота приложения
HEIGHT = 320

# Логотип приложения
ICON_URL = "icon/weather.png"

# My secret key (OpenWeather)
OPENWEATHER_API = ""

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
        "Санкт-Петербург"
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
    )
}
