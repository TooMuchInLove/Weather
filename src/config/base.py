from os import path as os_path
from os import environ as os_environ
from dataclasses import dataclass

# Секретный ключ (OpenWeather)
OPENWEATHER_API = os_environ.get("OPENWEATHER_API", "39ef5ab9b17a34d049087a678398ea89")
# Url-address (OpenWeather)
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?" \
                  f"lat=%s&lon=%s&appid={OPENWEATHER_API}&lang=ru&units=metric"

BACKSLASH_OS_WINDOWS = "\\"
# Текущая и основная рабочая директория
CURRENT_PATH = os_path.dirname(__file__)
MAIN_PATH = BACKSLASH_OS_WINDOWS.join(CURRENT_PATH.split(BACKSLASH_OS_WINDOWS)[:-2])
# Директория с логами
LOGS_PATH = f"{MAIN_PATH}\\logs"
# Директория с изображениями
IMAGES_PATH = f"{MAIN_PATH}\\icon"


@dataclass(slots=True, frozen=True)
class SettingsApplication:
    """ Настройки окна приложения """
    width: int = 600  # ширина окна приложения, 330
    height: int = 500  # высота окна приложения, 350
    height_widgets: int = 30  # высота компонентов в приложении
    margin: int = 20  # внутренняя рамка для окна приложения

    def size_widgets(self) -> tuple[int, int]:
        """ Размер виджета внутри приложения. """
        return self.width - self.margin, self.height_widgets


@dataclass(slots=True, frozen=True)
class ImagesApplication:
    """ Различные лого и иконки для приложения и виджетов """
    logo: str = f"{IMAGES_PATH}/weather.ico"
    icon_view: str = f"{IMAGES_PATH}/view.png"
    icon_update: str = f"{IMAGES_PATH}/update.png"
    icon_clear: str = f"{IMAGES_PATH}/clear.png"


settings_app = SettingsApplication()
images_app = ImagesApplication()


# Обнуление информации виджетах
EMPTY = ""
# Язык приложение
RU, ENG = "RU", "ENG"
LANGUAGE = RU

# TODO: тестовый вариант (переписать)
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
