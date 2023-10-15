# Локальные модули
from formUI import UiWeatherForm
from config import MAIN_CURRENT_PATH, LOCATION_STORAGE, LANGUAGE, EMPTY
from weather_gps import get_gps_coordinates
from weather_api_service import Weather, get_weather
from logging_ import TXTFileStorage, save_weather
from exceptions import (ErrorCountryDoesNotExist, ErrorCityDoesNotExist, ErrorApiService,
                        ErrorCantGetCoordinates, ErrorFileNotFound)


class LogicForm:
    def __init__(self) -> None:
        self.__ui = UiWeatherForm()  # Пользовательский интерфейс и компоненты
        self.__ui.listPlace.activated.connect(self.__event_clearing_data)  # События нажатия на кнопки
        self.__ui.bRequest.clicked.connect(self.__event_send_request)
        self.__ui.bClear.clicked.connect(self.__event_clearing_data)
        self.__ui.Timer.timeout.connect(self.__event_tick_timer)
        self.__set_place()  # Создаём раскрывающийся список

    def __event_tick_timer(self) -> None:
        """ Запуск таймера в приложении """
        self.__ui.Timer.stop()
        self.__ui.lNotification.setVisible(False)  # Убираем уведомление с экрана

    def __popup_notification(self, text: str) -> None:
        """ Устанавливаем текст/стиль/видимость для уведомления и запускаем таймер """
        self.__ui.lNotification.setText(text)
        self.__ui.lNotification.setVisible(True)
        self.__ui.Timer.start(1000)  # TIMEOUT

    def __set_place(self) -> None:
        """ Создаём раскрывающийся список стран-городов """
        for country, cities in LOCATION_STORAGE[LANGUAGE].items():
            for city in cities:
                self.__ui.listPlace.addItem(f"{country}, {city}")

    def __get_place(self) -> str:
        """ Возвращаем выбранное значение списка портов """
        return self.__ui.listPlace.currentText()

    def __event_send_request(self) -> None:
        # Получаем значение местаположения, разбиваем его на страну и город
        country, city = self.__get_place().split(", ")
        try:
            coordinates = get_gps_coordinates(country, city)  # Определяем координаты
            weather = get_weather(coordinates, country, city)  # Получаем данные о погоде
            self.__display_data(weather)  # Отображение результатов
            # Логгирование в текстовый документ
            save_weather(weather, TXTFileStorage(f"{MAIN_CURRENT_PATH}/logs/logging.txt"))
        except ErrorCountryDoesNotExist:
            self.__popup_notification(ErrorCountryDoesNotExist.error)
        except ErrorCityDoesNotExist:
            self.__popup_notification(ErrorCityDoesNotExist.error)
        except ErrorCantGetCoordinates:
            self.__popup_notification(ErrorCantGetCoordinates.error)
        except ErrorApiService:
            self.__popup_notification(ErrorApiService.error)
        except ErrorFileNotFound:
            self.__popup_notification(ErrorFileNotFound.error)

    def __display_data(self, weather: Weather) -> None:
        """ Получение и отображение результатов """
        self.__ui.lDataNow.setText(weather.date_now)
        self.__ui.lTemperature.setText(f"{weather.temperature}°C")
        self.__ui.lWeatherType.setText(f"{weather.weather_type}, {weather.description}")
        self.__ui.lHumidity.setText(f"Влажность {weather.humidity}%")
        self.__ui.lWindSpeed.setText(f"Скорость ветра {weather.wind_speed} м/с")
        self.__ui.lSunrise.setText(f"Восход {weather.sunrise}")
        self.__ui.lSunset.setText(f"Закат {weather.sunset}")

    def __event_clearing_data(self) -> None:
        """ Очистка данных в виджетов """
        self.__ui.lDataNow.setText(EMPTY)
        self.__ui.lTemperature.setText(EMPTY)
        self.__ui.lWeatherType.setText(EMPTY)
        self.__ui.lHumidity.setText(EMPTY)
        self.__ui.lWindSpeed.setText(EMPTY)
        self.__ui.lSunrise.setText(EMPTY)
        self.__ui.lSunset.setText(EMPTY)
