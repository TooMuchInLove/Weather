# # Определяем текущую директорию
# from pathlib import Path
# Локальные модули
from formUI import UiWeatherForm
from config import MAIN_CURRENT_PATH, LOCATION_STORAGE, EMPTY
from weather_gps import get_gps_coordinates
from weather_api_service import Weather, get_weather
from logging_ import TXTFileStorage, save_weather
from exceptions import (ErrorCountryDoesNotExist, ErrorCityDoesNotExist, ErrorApiService,
                        ErrorCantGetCoordinates, ErrorFileNotFound)


class LogicForm:
    def __init__(self) -> None:
        self.__ui = UiWeatherForm()  # Пользовательский интерфейс и компоненты
        self.__ui.listPlace.activated.connect(self.__clearing_data)  # События нажатия на кнопки
        self.__ui.bRequest.clicked.connect(self.__send_request)
        self.__errTimerCounter = 0  # Время для всплывающей панели ошибок
        self.__ui.Timer.timeout.connect(self.__tick)  # Запуск таймера, после установка метода .start()
        self.__set_place()  # Создаём раскрывающийся список

    def __tick(self) -> None:
        """ Включение таймера """
        self.__errTimerCounter += 1000  # Секунд прошло*
        if self.__errTimerCounter >= 3000:  # Если прошло N сек
            self.__errTimerCounter = 0  # Обнуляем счётчик и останавливаем таймер
            self.__ui.Timer.stop()
            self.__ui.lError.setVisible(False)  # Убираем ошибку с экрана
            self.__ui.bRequest.setEnabled(True)  # Активируем кнопку

    def __error(self, error) -> None:
        """ ... """
        self.__ui.lError.setText(error)  # Устанавливаем текст ошибки
        self.__ui.lError.setVisible(True)  # Отображение ошибки
        self.__ui.Timer.start(1000)  # Запуск таймера для отображения ошибки
        self.__ui.bRequest.setEnabled(False)  # На время ошибки блокируем кнопку

    def __set_place(self) -> None:
        """ Создаём раскрывающийся список стран-городов """
        for country, cities in LOCATION_STORAGE.items():
            for city in cities:
                self.__ui.listPlace.addItem(f"{country}, {city}")

    def __get_place(self) -> str:
        """ Возвращаем выбранное значение списка портов """
        return self.__ui.listPlace.currentText()

    def __send_request(self) -> None:
        # Получаем значение местаположения, разбиваем его на страну и город
        country, city = self.__get_place().split(", ")
        try:
            coordinates = get_gps_coordinates(country, city)  # Определяем координаты
            weather = get_weather(coordinates, country, city)  # Получаем данные о погоде
            self.__display_data(weather)  # Отображение результатов
            # Логгирование в текстовый документ
            save_weather(weather, TXTFileStorage(f"{MAIN_CURRENT_PATH}\logs\logging.txt"))
        except ErrorCountryDoesNotExist:
            self.__error(ErrorCountryDoesNotExist.error)
        except ErrorCityDoesNotExist:
            self.__error(ErrorCityDoesNotExist.error)
        except ErrorCantGetCoordinates:
            self.__error(ErrorCantGetCoordinates.error)
        except ErrorApiService:
            self.__error(ErrorApiService.error)
        except ErrorFileNotFound:
            self.__error(ErrorFileNotFound.error)

    def __display_data(self, weather: Weather) -> None:
        """ Получение и отображение результатов """
        self.__ui.lDataNow.setText(weather.date_now)
        self.__ui.lTemperature.setText(f"{weather.temperature}°C")
        self.__ui.lWeatherType.setText(f"{weather.weather_type}, {weather.description}")
        self.__ui.lHumidity.setText(f"Влажность: {weather.humidity}%")
        self.__ui.lWindSpeed.setText(f"Скорость ветра: {weather.wind_speed} м/с")
        self.__ui.lSunrise.setText(f"Восход: {weather.sunrise}")
        self.__ui.lSunset.setText(f"Закат: {weather.sunset}")

    def __clearing_data(self) -> None:
        """ Очистка данных в виджетов """
        self.__ui.lDataNow.setText(EMPTY)
        self.__ui.lTemperature.setText(EMPTY)
        self.__ui.lWeatherType.setText(EMPTY)
        self.__ui.lHumidity.setText(EMPTY)
        self.__ui.lWindSpeed.setText(EMPTY)
        self.__ui.lSunrise.setText(EMPTY)
        self.__ui.lSunset.setText(EMPTY)
