#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

from sys import exit, argv
from formUI import UiWindow
from form import LogicForm


if __name__ == "__main__":
    app = UiWindow(argv)  # Создание окна приложения
    ui = LogicForm()  # Пользовательский интерфейс и логика
    exit(app.exec_())  # Закрытие приложения по кнопке
