import peewee
from get_weather import WeatherMaker


class DatabaseUpdater:
    def __init__(self, bd):
        self.weather_list = None
        self.bd = bd

    def get_data(self, low_date, hi_date):
        """
        Поиск диапазона дат в базе дынных
        :param low_date: Старая дата
        :param hi_date: Более новая дата
        :return: Список данных за диапазон дат
        """
        data_from_database = []
        for weather_data in WeatherData.select().where(WeatherData.date.between(low_date, hi_date)):
            data_one_day = f'Погода {weather_data.weather},' \
                           f' температура {weather_data.temperature}, дата {weather_data.date}'
            data_from_database.append(data_one_day)
        return data_from_database

    def save_data(self, weather_list):
        """
        Сохранение полученых дат в базу данных
        :param weather_list: Список данных для сохранения
        :return: Информация о результате сохранения
        """
        for day_weather in weather_list:
            try:
                weather_bd = self.bd.create(weather=day_weather['Погода'],
                                            temperature=day_weather['Средняя температура'],
                                            date=day_weather['Дата'])
                weather_bd.save()
                return 'Данные успешно добавлены'
            except Exception as exc:
                return f'Данные не добавлены. Возникла проблема {exc}'


pg_db = peewee.PostgresqlDatabase('weather', user='postgres', password='postgres0987',
                                  host='', port=5432)


class BaseTable(peewee.Model):
    class Meta:
        database = pg_db


class WeatherData(BaseTable):
    weather = peewee.CharField()
    temperature = peewee.CharField()
    date = peewee.DateField(unique=True)


pg_db.create_tables([WeatherData])

if __name__ == '__main__':
    weather = WeatherMaker()

