from src.containers import Weather
from src.exc import ErrorFileNotFound


class IStorage:
    """ Интерфейс для любого хранилища, сохраняющего погоду """
    __slots__ = ()

    def save(self, weather: Weather) -> None:
        pass


class TXTFileStorage(IStorage):
    """ Хранилище данных в текстовом формате """
    __slots__ = ("_file",)

    def __init__(self, path: str) -> None:
        self._file = path

    def save(self, weather: Weather) -> None:
        try:
            output = output_weather(weather)
            with open(self._file, "a") as file:
                file.write(output)
        except FileNotFoundError:
            raise ErrorFileNotFound


def save_weather(weather: Weather, storage: IStorage) -> None:
    storage.save(weather)


def output_weather(weather: Weather) -> str:
    return f"\t{weather.date_now}\n" \
           f"\t{weather.place}\n" \
           f"\t\t{weather.temperature}°C\n" \
           f"\t{weather.weather_type}, {weather.description}\n" \
           f"\t|\tВлажность {weather.humidity}%\n" \
           f"\t|\tСкорость ветра {weather.wind_speed} м/с\n" \
           f"\t|\tВосход {weather.sunrise}\n" \
           f"\t|\tЗакат {weather.sunset}\n\n"


def output_weather_colors(weather: Weather) -> str:
    return f"\t\033[31m{weather.date_now}\033[0m\n" \
           f"\t{weather.place}\n" \
           f"\t\t\033[36m{weather.temperature}°C\033[0m\n" \
           f"\t{weather.weather_type}, {weather.description}\n" \
           f"\t\033[31m|\033[0m\tВлажность \033[34m{weather.humidity}%\033[0m\n" \
           f"\t\033[31m|\033[0m\tСкорость ветра \033[34m{weather.wind_speed}\033[0m м/с\n" \
           f"\t\033[31m|\033[0m\tВосход \033[34m{weather.sunrise}\033[0m\n" \
           f"\t\033[31m|\033[0m\tЗакат \033[34m{weather.sunset}\033[0m\n\n"
