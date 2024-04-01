#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

from sys import exit, argv
from ui import UiWindow
from services import LogicForm


if __name__ == "__main__":
    app = UiWindow(argv)
    ui = LogicForm()
    exit(app.exec_())
