from geopy.exc import GeocoderServiceError
from urllib.error import URLError


class ErrorCountryDoesNotExist(KeyError):
    """ Ошибка: страна не существует """
    __slots__ = ()

    error = "Ошибка! Указанная страна не найдена."


class ErrorCityDoesNotExist(KeyError):
    """ Ошибка: город не существует """
    __slots__ = ()

    error = "Ошибка! Указанный город не найден."


class ErrorCantGetCoordinates(ValueError):
    """ Ошибка: не смогли получить координаты """
    __slots__ = ()

    error = "Ошибка! Координаты не получены."


class ErrorApiService(URLError):
    """ Ошибка: неверный тип данных """
    __slots__ = ()

    error = "Ошибка! Вернулись не корректные данные."


class ErrorFileNotFound(FileNotFoundError):
    """ Ошибка: путь к файлу не найден """
    __slots__ = ()

    error = "Ошибка! Логгирование не выполнено."


class ErrorGeocoderService(GeocoderServiceError):
    """ Ошибка: подключение к интеренету """
    __slots__ = ()

    error = "Отсутствует подключение к интернету!"
