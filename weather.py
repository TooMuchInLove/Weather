#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

import sys
# Графический интерфейс
from PyQt5.QtWidgets import QWidget, QApplication

# Локальный config
from config import WIDTH, HEIGHT
# Графический интерфейс
from formUI import WeatherFormUI
# Логика приложения
from form import LogicForm


def main():
    # Создание приложения
    app = QApplication(sys.argv)
    Form = QWidget()
    # Пользовательский интерфейс GUI
    ui = WeatherFormUI(Form, WIDTH, HEIGHT)
    # Логика приложения
    login = LogicForm(ui)
    # Отображение формы
    Form.show()
    # Закрытие приложения по кнопке
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
