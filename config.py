# Определяем текущую директорию
from os import path as os_path

# Ширина и высота приложения
WIDTH, HEIGHT = 330, 350
# Высота компонентов приложения
HEIGHT_WIDGETS = 30
# Рамка приложения
MARGIN = 20
# Размер виджета
SIZE = (WIDTH - MARGIN, HEIGHT_WIDGETS)

# Текущая рабочая директория
MAIN_CURRENT_PATH = os_path.dirname(__file__)
# Логотип и иконки приложения
LOGO = f"{MAIN_CURRENT_PATH}/icon/weather.png"
ICON_VIEW = f"{MAIN_CURRENT_PATH}/icon/view.png"
ICON_UPDATE = f"{MAIN_CURRENT_PATH}/icon/update.png"
ICON_CLEAR = f"{MAIN_CURRENT_PATH}/icon/clear.png"

# Секретный ключ (OpenWeather)
OPENWEATHER_API = ""
# Url-address (OpenWeather)
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?"+\
                  f"lat=%s&lon=%s&appid={OPENWEATHER_API}&lang=ru&units=metric"

# Обнуление информации виджетах
EMPTY = ""
# Язык приложение
RU, ENG = "RU", "ENG"
LANGUAGE = RU

# Хранилище локаций (страна + город)
LOCATION_STORAGE = {
    RU: {
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
    },
    ENG: {
        "Russian": (
            "Moscow",
            "Saint-Petersburg",
            "Murino",
            "Rybinsk",
            "Yaroslavl",
        ),
        "Netherlands": (
            "Amsterdam",
        ),
        "Germany": (
            "Berlin",
        ),
        "Ireland": (
            "Dublin",
        ),
        "United Kingdom": (
            "London",
        ),
    },
}
