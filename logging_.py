# Локальный модули
from weather_api_service import Weather
from weather_output import output_weather
from exceptions import ErrorFileNotFound


class IStorage:
	""" Интерфейс для любого хранилища, сохраняющего погоду """
	__slots__ = ()

	def save(self, weather: Weather) -> None:
		pass


class TXTFileStorage(IStorage):
	""" Хранилище данных в текстовом формате """
	__slots__ = ("_file",)

	def __init__(self, path: str):
		self._file = path

	def save(self, weather: Weather) -> None:
		try:
			output = output_weather(weather)
			with open(self._file, "a") as file:
				file.write(output)
		except FileNotFoundError:
			raise ErrorFileNotFound


def save_weather(weather: Weather, storage: IStorage) -> None:
	storage.save(weather)
