from src.services import Weather
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
    return f"    {weather.date_now}\n" \
           f"    {weather.place}\n" \
           f"        {weather.temperature}°C\n" \
           f"    {weather.weather_type}, {weather.description}\n" \
           f"    |   Влажность {weather.humidity}%\n" \
           f"    |   Скорость ветра {weather.wind_speed} м/с\n" \
           f"    |   Восход {weather.sunrise}\n" \
           f"    |   Закат {weather.sunset}\n\n"


def output_weather_colors(weather: Weather) -> str:
    return f"    \033[31m{weather.date_now}\033[0m\n" \
           f"    {weather.place}\n" \
           f"        \033[36m{weather.temperature}°C\033[0m\n" \
           f"    {weather.weather_type}, {weather.description}\n" \
           f"    \033[31m|\033[0m   Влажность \033[34m{weather.humidity}%\033[0m\n" \
           f"    \033[31m|\033[0m   Скорость ветра \033[34m{weather.wind_speed}\033[0m м/с\n" \
           f"    \033[31m|\033[0m   Восход \033[34m{weather.sunrise}\033[0m\n" \
           f"    \033[31m|\033[0m   Закат \033[34m{weather.sunset}\033[0m\n\n"
