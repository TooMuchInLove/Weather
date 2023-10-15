# Графический интерфейс
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QRect, QTimer, QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QComboBox, QPushButton
# Локальные модули
from config import (SIZE, WIDTH, HEIGHT, HEIGHT_WIDGETS, MARGIN, LOGO,
                    ICON_VIEW, ICON_UPDATE, ICON_CLEAR)
from theme import DARK_THEME


class UiWindow(QApplication):
    """ Класс для создания окна приложения """
    __slots__ = ()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class UiWidget(QWidget):
    """ Класс общих параметров для виджетов """
    __slots__ = ()

    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(DARK_THEME)  # Стиль приложения и виджетов
        self.show()  # Отображение формы


class UiWeatherForm(UiWidget):
    """ Набор визуальных компонентов главного окна """
    __slots__ = ("lDataNow", "listPlace", "lTemperature", "lWeatherType", "lHumidity", "lWindSpeed",
                 "lSunrise", "lSunset", "bRequest", "bSettings", "gridlayout", "lNotification", "Timer",)

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Погода")  # Отображение название в объектах
        self.setMinimumSize(QSize(WIDTH, HEIGHT))  # Минимальный размер окна
        self.setMaximumSize(QSize(WIDTH, HEIGHT))  # Максимальный размер окна
        self.setWindowIcon(QIcon(LOGO))  # Логотип приложения
        self.setStyleSheet(DARK_THEME)  # Стиль приложения и виджетов
        self.__setup_ui()
        self.__setup_font()
        self.__setup_object_names()

    def __setup_ui(self) -> None:
        """ Настройка и создание виджетов приложения """
        self.lDataNow = QLabel()  # Лэйбл для отображения Даты и Времени
        self.lDataNow.setMinimumSize(QSize(*SIZE))
        self.listPlace = QComboBox()  # Лэйбл для отображения Места проживания
        self.listPlace.setMaxVisibleItems(5)
        self.listPlace.setMinimumSize(QSize(*SIZE))
        self.lTemperature = QLabel()  # Лэйбл для отображения Температуры
        self.lTemperature.setAlignment(Qt.AlignCenter)
        self.lTemperature.setMinimumSize(QSize(*SIZE))
        self.lWeatherType = QLabel()  # Лэйбл для отображения Типа Погоды
        self.lWeatherType.setMinimumSize(QSize(*SIZE))
        self.lHumidity = QLabel()  # Лэйбл для отображения Влажности
        self.lHumidity.setMinimumSize(QSize(*SIZE))
        self.lWindSpeed = QLabel()  # Лэйбл для отображения Скорости ветра
        self.lWindSpeed.setMinimumSize(QSize(*SIZE))
        self.lSunrise = QLabel()  # Лэйбл для отображения Восхода
        self.lSunrise.setMinimumSize(QSize(*SIZE))
        self.lSunset = QLabel()  # Лэйбл для отображения Заката
        self.lSunset.setMinimumSize(QSize(*SIZE))
        self.bRequest = QPushButton()  # Кнопка обновления данных
        self.bRequest.setIcon(QIcon(ICON_VIEW))
        self.bRequest.setMinimumSize(QSize(HEIGHT_WIDGETS, HEIGHT_WIDGETS))
        self.bSettings = QPushButton()  # Кнопка настройки данных
        self.bSettings.setIcon(QIcon(ICON_UPDATE))
        self.bSettings.setMinimumSize(QSize(HEIGHT_WIDGETS, HEIGHT_WIDGETS))
        self.bClear = QPushButton()  # Кнопка очистки содержимого виджетов
        self.bClear.setIcon(QIcon(ICON_CLEAR))
        self.bClear.setMinimumSize(QSize(HEIGHT_WIDGETS, HEIGHT_WIDGETS))
        self.gridlayout = QGridLayout(self)  # Разметка виджетов приложения
        self.gridlayout.addWidget(self.lDataNow, 1, 0, 1, 3)
        self.gridlayout.addWidget(self.listPlace, 2, 0, 1, 3)
        self.gridlayout.addWidget(self.lTemperature, 3, 0, 1, 3)
        self.gridlayout.addWidget(self.lWeatherType, 4, 0, 1, 3)
        self.gridlayout.addWidget(self.lHumidity, 5, 0, 1, 3)
        self.gridlayout.addWidget(self.lWindSpeed, 6, 0, 1, 3)
        self.gridlayout.addWidget(self.lSunrise, 7, 0, 1, 3)
        self.gridlayout.addWidget(self.lSunset, 8, 0, 1, 3)
        self.gridlayout.addWidget(self.bSettings, 9, 0, alignment=Qt.AlignRight | Qt.AlignTop)
        self.gridlayout.addWidget(self.bRequest, 9, 1, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.gridlayout.addWidget(self.bClear, 9, 2, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.lNotification = QLabel(self)  # Лэйбл для отображения ошибок
        self.lNotification.setGeometry(QRect(5, 5, WIDTH-MARGIN, HEIGHT_WIDGETS))
        self.lNotification.setVisible(False)
        self.Timer = QTimer()  # Таймер, уделённый под ошибку

    def __setup_font(self) -> None:
        """ Настройка стиля шрифта и размера """
        font_group1 = QFont()  # Группа 1
        font_group1.setFamily("Consolas")  # Rockwell, Arial, Consolas
        font_group1.setPointSize(13)
        font_group2 = QFont()   # Группа 2
        font_group2.setFamily("Consolas")
        font_group2.setPointSize(10)
        self.setFont(font_group1)  # Стиль шрифта и размер
        self.lDataNow.setFont(font_group1)
        self.listPlace.setFont(font_group1)
        self.lTemperature.setFont(font_group1)
        self.lWeatherType.setFont(font_group2)
        self.lHumidity.setFont(font_group2)
        self.lWindSpeed.setFont(font_group2)
        self.lSunrise.setFont(font_group2)
        self.lSunset.setFont(font_group2)
        self.bRequest.setFont(font_group1)
        self.bSettings.setFont(font_group1)
        self.lNotification.setFont(font_group2)

    def __setup_object_names(self) -> None:
        """ Настройка и установка имён для виджетов """
        self.lDataNow.setObjectName("lDataNow")
        self.listPlace.setObjectName("lPlace")
        self.lTemperature.setObjectName("lTemperature")
        self.lWeatherType.setObjectName("lWeatherType")
        self.lHumidity.setObjectName("lHumidity")
        self.lWindSpeed.setObjectName("lWindSpeed")
        self.lSunrise.setObjectName("lSunrise")
        self.lSunset.setObjectName("lSunset")
        self.bRequest.setObjectName("bRequest")
        self.lNotification.setObjectName("lNotification")

    def close(self) -> None:
        """ Закрытие окна приложения """
        QCoreApplication.instance().quit()
