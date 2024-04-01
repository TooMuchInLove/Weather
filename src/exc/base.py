# FIXME: исправить все Exception на более подробные исключения

class ErrorCountryDoesNotExist(Exception):
    """ Ошибка: страна не существует """
    error = "Извините! Не смог найти такую страну."


class ErrorCityDoesNotExist(Exception):
    """ Ошибка: город не существует """
    error = "Извините! Не смог найти такой город."


class ErrorCantGetCoordinates(Exception):
    """ Ошибка: не смогли получить координаты """
    error = "Извините! Не смог получить координаты."


class ErrorApiService(Exception):
    """ Ошибка: неверный тип данных """
    error = "Извините! Вернулись не корректные данные."


class ErrorFileNotFound(FileNotFoundError):
    """ Ошибка: путь к файлу не найден """
    error = "Извините! Не смог выполнить логгирование."
