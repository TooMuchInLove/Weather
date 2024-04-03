from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QRect, QTimer, QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QComboBox, QPushButton
from src.config import settings_app as sapp, images_app as iapp
from .theme import DARK_THEME


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
        self.setStyleSheet(DARK_THEME)
        self.show()


class UiWeatherForm(UiWidget):
    """ Набор визуальных компонентов главного окна """
    __slots__ = ("lDataNow", "listPlace", "lTemperature", "lWeatherType", "lHumidity", "lWindSpeed",
                 "lSunrise", "lSunset", "bRequest", "bSettings", "gridlayout", "lNotification", "Timer",)

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(sapp.title)
        self.setMinimumSize(QSize(sapp.width, sapp.height))
        self.setMaximumSize(QSize(sapp.width, sapp.height))
        self.setWindowIcon(QIcon(iapp.logo))
        self.setStyleSheet(DARK_THEME)
        self.__setup_ui()

    def __setup_ui(self) -> None:
        """ Настройка и создание виджетов приложения """
        font_group1 = QFont("Consolas", 10)  # Rockwell, Arial, Consolas
        font_group2 = QFont("Consolas", 8)
        self.setFont(font_group1)
        self.Timer = QTimer()
        self.listPlace = QComboBox()
        self.listPlace.setMaxVisibleItems(5)
        self.listPlace.setMinimumSize(QSize(*sapp.size_widgets()))
        self.listPlace.setObjectName("lPlace")
        self.listPlace.setFont(font_group1)
        self.lDataNow = Label(*sapp.size_widgets(), font=font_group1, name="lDataNow")
        self.lTemperature = Label(*sapp.size_widgets(), font=font_group1, name="lTemperature", align=1)
        self.lWeatherType = Label(*sapp.size_widgets(), font=font_group2, name="lWeatherType")
        self.lHumidity = Label(*sapp.size_widgets(), font=font_group2, name="lHumidity")
        self.lWindSpeed = Label(*sapp.size_widgets(), font=font_group2, name="lWindSpeed")
        self.lSunrise = Label(*sapp.size_widgets(), font=font_group2, name="lSunrise")
        self.lSunset = Label(*sapp.size_widgets(), font=font_group2, name="lSunset")
        self.bRequest = PushButton(sapp.height_widgets, sapp.height_widgets, name="bRequest", icon=iapp.icon_view)
        self.bSettings = PushButton(sapp.height_widgets, sapp.height_widgets, name="qwe", icon=iapp.icon_update)
        self.bClear = PushButton(sapp.height_widgets, sapp.height_widgets, name="qwe", icon=iapp.icon_clear)
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
        self.lNotification = QLabel(self)
        self.lNotification.setGeometry(QRect(10, 10, sapp.width - 20, sapp.height_widgets))
        self.lNotification.setWordWrap(True)
        self.lNotification.setVisible(False)
        self.lNotification.setObjectName("lNotification")
        self.lNotification.setFont(font_group2)

    def close(self) -> None:
        """ Закрытие окна приложения """
        QCoreApplication.instance().quit()


class Label(QLabel):
    def __init__(self, width: int, height: int, font: QFont = None, name: str = None, align: int = None) -> None:
        QLabel.__init__(self)
        self.setMinimumSize(QSize(width, height))
        if font is not None:
            self.setFont(font)
        if name is not None:
            self.setObjectName(name)
        if align is not None:
            alignments = {0: Qt.AlignLeft, 1: Qt.AlignCenter, 2: Qt.AlignRight}
            self.setAlignment(alignments[align])


class PushButton(QPushButton):
    def __init__(self, width: int, height: int, name: str = None, icon: str = None) -> None:
        QPushButton.__init__(self)
        self.setMinimumSize(QSize(width, height))
        if name is not None:
            self.setObjectName(name)
        if icon is not None:
            self.setIcon(QIcon(icon))
