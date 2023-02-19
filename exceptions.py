# -*- coding: utf-8 -*-


class ErrorCountryDoesNotExist(Exception):
    """ Ошибка: страна не существует """
    def __init__(self):
        self.__error_message = "Извините! Не смог найти такую страну."
        self.__error()

    def __error(self):
        print(self.__error_message)


class ErrorCityDoesNotExist(Exception):
    """ Ошибка: город не существует """
    def __init__(self):
        self.__error_message = "Извините! Не смог найти такой город."
        self.__error()

    def __error(self):
        print(self.__error_message)


class ErrorCantGetCoordinates(Exception):
    """ Ошибка: не смогли получить координаты """
    def __init__(self):
        self.__error_message = "Извините! Не смог получить координаты."
        self.__error()

    def __error(self):
        print(self.__error_message)


class ErrorApiService(Exception):
    """ Ошибка: неверный тип данных """
    def __init__(self):
        self.__error_message = "Извините! Вернулись не корректные данные."
        self.__error()

    def __error(self):
        print(self.__error_message)
