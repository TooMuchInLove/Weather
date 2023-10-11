# Графический интерфейс
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QRect, QTimer, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLabel,
                             QComboBox, QPushButton, QToolButton)
# Локальные модули
from config import ICON_URL, SIZE, WIDTH, HEIGHT, HEIGHT_WIDGETS, MARGIN
from theme import DARK_THEME


class UiWindow(QApplication):
    """ Класс для создания окна приложения """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class UiWidget(QWidget):
    """ Класс общих параметров для виджетов """
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(DARK_THEME)  # Стиль приложения и виджетов
        self.show()  # Отображение формы


class UiWeatherForm(UiWidget):
    """ Набор визуальных компонентов главного окна """
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Погода")  # Отображение название в объектах
        self.setMinimumSize(QSize(WIDTH, HEIGHT))  # Минимальный размер окна
        self.setMaximumSize(QSize(WIDTH, HEIGHT))  # Максимальный размер окна
        self.setWindowIcon(QIcon(ICON_URL))  # Логотип приложения
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
        self.bRequest.setText("Запросить")
        self.bRequest.setMinimumSize(QSize(int(WIDTH/2)-MARGIN, HEIGHT_WIDGETS))
        self.bSettings = QToolButton()  # Кнопка настройки данных
        self.bSettings.setText("...")
        self.bSettings.setMinimumSize(QSize(int(WIDTH/2)-MARGIN, HEIGHT_WIDGETS))
        self.gridlayout = QGridLayout(self)  # Разметка виджетов приложения
        self.gridlayout.addWidget(self.lDataNow, 1, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.listPlace, 2, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.lTemperature, 3, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.lWeatherType, 4, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.lHumidity, 5, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.lWindSpeed, 6, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.lSunrise, 7, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.lSunset, 8, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.bRequest, 9, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.bSettings, 9, 1, alignment=Qt.AlignRight | Qt.AlignTop)
        self.lError = QLabel(self)  # Лэйбл для отображения ошибок
        self.lError.setGeometry(QRect(5, 5, WIDTH-MARGIN, HEIGHT_WIDGETS))
        self.lError.setVisible(False)
        self.Timer = QTimer()  # Таймер, уделённый под ошибку
        QMetaObject.connectSlotsByName(self)

    def __setup_font(self) -> None:
        """ Настройка стиля шрифта и размера """
        font_group1 = QFont()  # Группа 1
        font_group1.setFamily("Consolas")  # Rockwell, Arial, Consolas
        font_group1.setPointSize(13)
        font_group2 = QFont()   # Группа 2
        font_group2.setFamily("Consolas")
        font_group2.setPointSize(10)
        # self.setFont(font_group1)  # Стиль шрифта и размер
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
        self.lError.setFont(font_group2)

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
        self.bSettings.setObjectName("bSettings")
        self.lError.setObjectName("lError")

    def close(self) -> None:
        """ Закрытие окна приложения """
        QCoreApplication.instance().quit()
