# -*- coding: utf-8 -*-


class ErrorCountryDoesNotExist(Exception):
    """ Ошибка: страна не существует """
    error = "Извините! Не смог найти такую страну."
    # def __init__(self):
    #     self.__error_message = "Извините! Не смог найти такую страну."
    #     self.__error()
    #
    # def __error(self):
    #     print(self.__error_message)


class ErrorCityDoesNotExist(Exception):
    """ Ошибка: город не существует """
    error = "Извините! Не смог найти такой город."


class ErrorCantGetCoordinates(Exception):
    """ Ошибка: не смогли получить координаты """
    error = "Извините! Не смог получить координаты."


class ErrorApiService(Exception):
    """ Ошибка: неверный тип данных """
    error = "Извините! Вернулись не корректные данные."


class ErrorFileNotFound(Exception):
    """ Ошибка: путь к файлу не найден """
    error = "Извините! Не смог выполнить логгирование."
