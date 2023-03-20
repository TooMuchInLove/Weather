# -*- coding: utf-8 -*-

# Определяем текущую директорию
from pathlib import Path

# Локальный config
from config import LOCATION_STORAGE
# Локальный модули
from weather_gps import set_location
from weather_gps import get_gps_coordinates
from weather_api_service import get_weather
from weather_api_service import Weather
from logging_ import save_weather, TXTFileStorage
# Локальные исключения
from exceptions import ErrorCountryDoesNotExist
from exceptions import ErrorCityDoesNotExist
from exceptions import ErrorCantGetCoordinates
from exceptions import ErrorApiService
from exceptions import ErrorFileNotFound


class LogicForm:
    def __init__(self, _ui):
        # Пользовательский интерфейс и компоненты
        self.__ui = _ui
        # События нажатия на кнопки
        self.__ui.listPlace.activated.connect(self.__clearing_data)
        self.__ui.bRequest.clicked.connect(self.__send_request)
        # self.__ui.bClose.clicked.connect(self.__ui.close)
        # Время для всплывающей панели ошибок
        self.__errTimerCounter = 0
        # Время в 1000 = 1сек
        self.__TIME_OUT = 1000
        # Запуск таймера, после установка метода .start()
        self.__ui.Timer.timeout.connect(self.__tick)
        # Создаём раскрывающийся список
        self.__set_place()

    def __tick(self):
        # Секунд прошло*
        self.__errTimerCounter += self.__TIME_OUT
        # Если прошло N сек
        if self.__errTimerCounter >= self.__TIME_OUT*3:
            # Обнуляем счётчик и останавливаем таймер
            self.__errTimerCounter = 0
            self.__ui.Timer.stop()
            # Убираем ошибку с экрана
            self.__ui.lError.setVisible(False)
            # Активируем кнопку
            self.__ui.bRequest.setEnabled(True)

    def __error(self, _error):
        # Устанавливаем текст ошибки
        self.__ui.lError.setText(_error)
        # Отображение ошибки
        self.__ui.lError.setVisible(True)
        # Запуск таймера для отображения ошибки
        self.__ui.Timer.start(self.__TIME_OUT)
        # На время ошибки блокируем кнопку
        self.__ui.bRequest.setEnabled(False)

    def __set_place(self):
        # Создаём раскрывающийся список стран-городов
        for country, cities in LOCATION_STORAGE.items():
            for city in cities:
                self.__ui.listPlace.addItem("%s, %s" % (country, city))

    def __get_place(self) -> str:
        # Возвращаем выбранное значение списка портов
        return self.__ui.listPlace.currentText()

    def __send_request(self):
        # Получаем значение местаположения, разбиваем его на страну и город
        country, city = self.__get_place().split(", ")
        try:
            # Определяем местоположение
            set_location(country, city)
            # Определяем координаты
            coordinates = get_gps_coordinates()
            # Получаем данные о погоде
            weather = get_weather(coordinates, country, city)
            # Отображение результатов
            self.__display_data(weather)
            # Логгирование в текстовый документ
            save_weather(weather, TXTFileStorage(Path.cwd()/"logs\logging.txt"))
        except ErrorCountryDoesNotExist:
            self.__error(ErrorCountryDoesNotExist.error)
            # ErrorQLabel(self.__ui, ErrorCountryDoesNotExist.error)
        except ErrorCityDoesNotExist:
            self.__error(ErrorCityDoesNotExist.error)
            # ErrorQLabel(self.__ui, ErrorCityDoesNotExist.error)
        except ErrorCantGetCoordinates:
            self.__error(ErrorCantGetCoordinates.error)
            # ErrorQLabel(self.__ui, ErrorCantGetCoordinates.error)
        except ErrorApiService:
            self.__error(ErrorApiService.error)
            # ErrorQLabel(self.__ui, ErrorApiService.error)
        except ErrorFileNotFound:
            self.__error(ErrorFileNotFound.error)
            # ErrorQLabel(self.__ui, ErrorFileNotFound.error)

    def __display_data(self, _weather: Weather):
        # Получение и отображение результатов
        self.__ui.lDataNow.setText("%s" % (_weather.date_now))
        self.__ui.lTemperature.setText("%s°C" % (_weather.temperature))
        self.__ui.lWeatherType.setText("%s, %s" % (_weather.weather_type, _weather.description))
        self.__ui.lHumidity.setText("Влажность: %s%%" % (_weather.humidity))
        self.__ui.lWindSpeed.setText("Скорость ветра: %s м/с" % (_weather.wind_speed))
        self.__ui.lSunrise.setText("Восход: %s" % (_weather.sunrise))
        self.__ui.lSunset.setText("Закат: %s" % (_weather.sunset))

    def __clearing_data(self):
        # Очистка данных
        empty = ""
        self.__ui.lDataNow.setText(empty)
        self.__ui.lTemperature.setText(empty)
        self.__ui.lWeatherType.setText(empty)
        self.__ui.lHumidity.setText(empty)
        self.__ui.lWindSpeed.setText(empty)
        self.__ui.lSunrise.setText(empty)
        self.__ui.lSunset.setText(empty)
