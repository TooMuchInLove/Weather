# Определяем текущую директорию
from os import getcwd as os_get_cwd

# Ширина и высота приложения
WIDTH, HEIGHT = 330, 350
# Высота компонентов приложения
HEIGHT_WIDGETS = 30
# Рамка приложения
MARGIN = 20
# Размер виджета
SIZE = (WIDTH - MARGIN, HEIGHT_WIDGETS)
# Текущая рабочая директория
MAIN_CURRENT_PATH = os_get_cwd()
# Логотип приложения
ICON_URL = "icon/weather.png"
# Секретный ключ (OpenWeather)
OPENWEATHER_API = "39ef5ab9b17a34d049087a678398ea89"
# Url-address (OpenWeather)
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?"+\
                  f"lat=%s&lon=%s&appid={OPENWEATHER_API}&lang=ru&units=metric"
# Обнуление информации виджетах
EMPTY = ""
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
