# -*- coding: utf-8 -*-

# Определяем текущую директорию
from pathlib import Path

# Локальный модули
from weather_api_service import Weather
from weather_output import output_weather


class Storage:
	""" Интерфейс для любого хранилища, сохраняющего погоду """
	def save(self, _weather: Weather) -> None:
		pass


class TXTFileStorage(Storage):
	""" Хранилище данных в текстовом формате """
	def __init__(self, _file: Path):
		self._file = _file

	def save(self, _weather: Weather) -> None:
		output = output_weather(_weather)
		with open(self._file, "a") as file:
			file.write("%s" % (output))


def save_weather(_weather: Weather, _storage: Storage) -> None:
	_storage.save(_weather)
