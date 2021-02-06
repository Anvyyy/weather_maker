# -*- coding: utf-8 -*-
import argparse
from datetime import datetime, timedelta

from get_weather import WeatherMaker
from image_maker import ImageMaker
from data_base import DatabaseUpdater, WeatherData


class Manager:
    def __init__(self, weather, image_maker, bd):
        self.weather = weather
        self.image_maker = image_maker
        self.data_base = bd
        self.list_weather = []

    def pars_weather(self):
        """
        Выводит на консоль информацию за последние 7 дней
        :return: None
        """
        for i in self.list_weather:
            for key, value in enumerate(i.items()):
                print(f'{value[0]}, {value[1]}')
            print('')

    def postcard(self):
        """
        Создает погодные открытки
        :return: None
        """
        self.image_maker.creating_weather_image(self.list_weather)

    def add_to_bd(self):
        """
        Сохраняет полученные данные
        :return: Данные успешно добавлены
        """
        return self.data_base.save_data(weather_list=self.list_weather)

    def user_date(self, low_date, hi_date):
        """
        Выводит погоду за указанный пользователем диапазон дат
        :param low_date: Старая дата
        :param hi_date: Более новая дата
        :return: None
        """
        for weather_one_day in self.data_base.get_data(low_date, hi_date):
            print(weather_one_day)

    def load_weather_week(self):
        """
        При запуске программы парсит погодные данные за последние 7 дней
        :return: None
        """
        date_list = []
        date_format = '%Y.%m.%d'
        today = datetime.now()
        for days in range(7):
            last_day = today + timedelta(days=-days)
            date_list.append(last_day.strftime(date_format))
        self.list_weather = self.weather.get_weather(date_list=date_list)


def create_parser():
    """
    Создание консольных команд
    :return: Объект для разбора строк командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-pars', '--pars_weather', action='store_true')  # Показ погоды в консоли
    parser.add_argument('-card', '--postcard', action='store_true')  # Создание открыток
    parser.add_argument('-bd', '--add_to_bd', action='store_true')  # Добавление дат в базу данных
    parser.add_argument('-get', '--get_data', action='store_true')  # Вывести данные из базы данных
    parser.add_argument('-low', '--low_date')  # Начальная дата
    parser.add_argument('-hi', '--hi_date')  # Конечная дата
    # добавить тип даты
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args_space = parser.parse_args()
    manage = Manager(weather=WeatherMaker(), image_maker=ImageMaker(), bd=DatabaseUpdater(bd=WeatherData))
    manage.load_weather_week()

    if args_space.pars_weather:
        manage.pars_weather()
    if args_space.postcard:
        manage.postcard()
    if args_space.add_to_bd:
        print(manage.add_to_bd())
    if args_space.get_data:
        manage.user_date(low_date=args_space.low_date, hi_date=args_space.hi_date)