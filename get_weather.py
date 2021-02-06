import bs4

import requests


class WeatherMaker:
    def __init__(self):
        self.temp = None

    def get_weather(self, date_list):
        """
        Парсинг данных о погоде
        :param date_list: Список дат
        :return: Список данных о погоде
        """
        weather_list = []
        for days in date_list:
            url = f'https://darksky.net/details/55.7616,37.6095/{days}/ca12/en'
            response = requests.get(url).text
            soup = bs4.BeautifulSoup(response, 'html.parser')
            all_temp = soup.find_all('span', {'class': 'temp'})
            # all_time = soup.find_all('span', {'class': 'time'})
            all_weather = soup.find('span', {'class': 'label swip'})
            average_temperature = []
            for temp in all_temp:
                average_temperature.append(int(temp.text.split('˚')[0]))
                self.temp = sum(average_temperature) / 2
            average_temperature.clear()
            weather_list += [{'Дата': days, 'Погода': all_weather.text, 'Средняя температура': str(self.temp) + "˚"}]
        return weather_list


if __name__ == '__main__':
    weather = WeatherMaker()

