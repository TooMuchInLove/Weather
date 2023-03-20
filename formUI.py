# -*- coding: utf-8 -*-

# Графический интерфейс
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QRect, QTimer
from PyQt5.QtCore import QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QComboBox
from PyQt5.QtWidgets import QPushButton, QToolButton

# Локальный config
from config import ICON_URL
# Тема приложения
from theme import DARK_THEME


class WeatherFormUI(object):
    def __init__(self, _widget, _w, _h):
        # Определяем виджеты
        self.widget = _widget
        # Ширина приложения
        self.WIDTH = _w
        # Высота приложения
        self.HEIGHT = _h
        # Определяем параметры виджета и заголовки компонентов
        self.__setupUi()
        self.__retranslateUi()

    def __setupUi(self):
        # Стиль шрифта и размер
        # Группа 1
        font_group1 = QFont()
        font_group1.setFamily("Rockwell")
        font_group1.setPointSize(13)
        # Группа 2
        font_group2 = QFont()
        font_group2.setFamily("Consolas")
        font_group2.setPointSize(10)
        # Группа 3
        font_group3 = QFont()
        font_group3.setFamily("Consolas")
        font_group3.setPointSize(10)
        # Название приложения
        self.widget.setObjectName("WeatherForm")
        # Логотип приложения
        self.widget.setWindowIcon(QIcon(ICON_URL))
        # Размер приложения
        self.widget.resize(self.WIDTH, self.HEIGHT)
        # Стиль шрифта и размер
        self.widget.setFont(font_group1)
        # Стиль приложения и виджетов
        self.widget.setStyleSheet(DARK_THEME)
        # Максимальный и минимальный размер окна
        self.widget.setMinimumSize(QSize(self.WIDTH, self.HEIGHT))
        self.widget.setMaximumSize(QSize(self.WIDTH, self.HEIGHT))
        # Виджет для расположения объектов
        self.__MainWidget = QWidget(self.widget)
        # Размеры и расположение
        XMP, YMP, WMP, HMP = 10, 10, self.WIDTH-20, self.HEIGHT-50
        self.__MainWidget.setGeometry(QRect(XMP, YMP, WMP, HMP))
        self.__MainWidget.setObjectName("__MainWidget")
        # Слой с компонентами основной панели
        self.__LayoutForPanel = QVBoxLayout(self.__MainWidget)
        self.__LayoutForPanel.setObjectName("__LayoutForPanel")
        # Лэйбл для отображения Даты и Времени
        self.lDataNow = QLabel(self.__MainWidget)
        self.lDataNow.setFont(font_group1)
        self.lDataNow.setObjectName("lDataNow")
        # Лэйбл для отображения Места проживания
        self.listPlace = QComboBox(self.__MainWidget)
        self.listPlace.setMaxVisibleItems(5)
        self.listPlace.setFont(font_group1)
        self.listPlace.setObjectName("lPlace")
        # Лэйбл для отображения Температуры
        self.lTemperature = QLabel(self.__MainWidget)
        self.lTemperature.setFont(font_group1)
        self.lTemperature.setAlignment(Qt.AlignCenter)
        self.lTemperature.setObjectName("lTemperature")
        # Лэйбл для отображения Типа Погоды
        self.lWeatherType = QLabel(self.__MainWidget)
        self.lWeatherType.setFont(font_group1)
        self.lWeatherType.setObjectName("lWeatherType")
        # Лэйбл для отображения Влажности
        self.lHumidity = QLabel(self.__MainWidget)
        self.lHumidity.setFont(font_group2)
        self.lHumidity.setObjectName("lHumidity")
        # Лэйбл для отображения Скорости ветра
        self.lWindSpeed = QLabel(self.__MainWidget)
        self.lWindSpeed.setFont(font_group2)
        self.lWindSpeed.setObjectName("lWindSpeed")
        # Лэйбл для отображения Восхода
        self.lSunrise = QLabel(self.__MainWidget)
        self.lSunrise.setFont(font_group2)
        self.lSunrise.setObjectName("lSunrise")
        # Лэйбл для отображения Заката
        self.lSunset = QLabel(self.__MainWidget)
        self.lSunset.setFont(font_group2)
        self.lSunset.setObjectName("lSunset")
        # Компоновка объектов на панели
        self.__LayoutForPanel.addWidget(self.lDataNow)
        self.__LayoutForPanel.addWidget(self.listPlace)
        self.__LayoutForPanel.addWidget(self.lTemperature)
        self.__LayoutForPanel.addWidget(self.lWeatherType)
        self.__LayoutForPanel.addWidget(self.lHumidity)
        self.__LayoutForPanel.addWidget(self.lWindSpeed)
        self.__LayoutForPanel.addWidget(self.lSunrise)
        self.__LayoutForPanel.addWidget(self.lSunset)
        # Кнопка обновления данных
        self.bRequest = QPushButton(self.widget)
        # Размеры и расположение
        WBR, HBR = 150, 30
        XBR, YBR = int((self.WIDTH/2)-(WBR/2)), YMP+HMP
        self.bRequest.setGeometry(QRect(XBR, YBR, WBR, HBR))
        self.bRequest.setFont(font_group1)
        self.bRequest.setObjectName("bRequest")
        # Кнопка настройки данных
        self.bSettings = QToolButton(self.widget)
        # Размеры и расположение
        WBS, HBS = 30, 30
        XBS, YBS = XBR+WBR+5, YBR
        self.bSettings.setGeometry(QRect(XBS, YBS, WBS, HBS))
        self.bSettings.setFont(font_group1)
        self.bSettings.setObjectName("bSettings")

        # # Кнопка закрытия
        # self.bClose = QToolButton(self.widget)
        # # Размеры и расположение
        # WBS, HBS = 30, 30
        # XBS, YBS = XBR-WBS-5, YBR
        # self.bClose.setGeometry(QRect(XBS, YBS, WBS, HBS))
        # self.bClose.setFont(font_group1)
        # self.bClose.setObjectName("bClose")

        # Лэйбл для отображения ошибок
        self.lError = QLabel(self.widget)
        self.lError.setGeometry(QRect(5, 5, self.WIDTH-10, HBS))
        self.lError.setFont(font_group3)
        self.lError.setObjectName("lError")
        self.lError.setVisible(False)

        # Таймер, уделённый под ошибку
        self.Timer = QTimer()
        # ...
        QMetaObject.connectSlotsByName(self.widget)

    def __retranslateUi(self):
        # Отображение название в объектах
        self.widget.setWindowTitle("Погода")
        # self.bClose.setText("х")
        self.bRequest.setText("Запросить")
        self.bSettings.setText("...")

    def close(self):
        # Закрытие окна приложения
        QCoreApplication.instance().quit()


class ErrorQLabel:
    def __init__(self, _ui, _error):
        # Пользовательский интерфейс и компоненты
        self.__ui = _ui

        # Лэйбл для отображения ошибок
        WLE, HLE = self.__ui.WIDTH-10, 30
        XLE, YLE = 5, 5
        self.lError = QLabel(self.__ui.widget)
        self.lError.setGeometry(QRect(XLE, YLE, WLE, HLE))
        self.lError.setText(_error)
        # self.lError.setFont(font_group3)
        self.lError.setObjectName("lError")

        # Размеры и расположение
        self.bClose = QLabel(self.__ui.widget)
        self.bClose.setGeometry(QRect(XLE+WLE-10, YLE*2, 10, 10))
        self.bClose.setText("х")
        # self.bClose.setFont(font_group1)
        self.bClose.setObjectName("bClose")
        self.bClose.setVisible(False)
