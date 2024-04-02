#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

from sys import exit, argv
from ui import UiWindow
from services import LogicForm


def main() -> None:
    app = UiWindow(argv)
    _ = LogicForm()  # var ui
    exit(app.exec_())


if __name__ == "__main__":
    main()
