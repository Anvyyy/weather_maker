import os

import cv2

from get_weather import WeatherMaker

IMAGE = 'photo/probe.jpg'


class ImageMaker:
    def __init__(self, image_location=IMAGE):
        self.background = cv2.imread(image_location)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.coordinate_list = [(400, 50), (400, 100), (150, 50)]
        self.text_list = ['Погода', 'Средняя температура', 'Дата']
        self.fontScale = 1
        self.color = (0, 0, 0)
        self.thickness = 2
        self.weather_postcard = None

    def view_image(self, image, name_of_window):
        """Показ на экране"""
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def creating_weather_image(self, weather_list):
        """Начало создания открытки с погодой"""
        file_location = {
            'Snow': 'python_snippets/external_data/weather_img/snow.jpg',
            'Rain': 'python_snippets/external_data/weather_img/rain.jpg',
            'Sun': 'photo/sun.png',
            'Cloud': 'photo/cloud.png'
        }
        for weather_data in weather_list:
            img = cv2.imread(file_location[weather_data['Погода']])
            self.drawing_postcard(image=img, weather_data=weather_data)

    def text_on_postcard(self, text, coordinates, background):
        """Печать текста на открытку"""
        background = cv2.putText(background, text, coordinates, self.font,
                                 self.fontScale, self.color, self.thickness, cv2.FONT_HERSHEY_COMPLEX)
        return background

    def drawing_postcard(self, image, weather_data):
        """Создание открытки и добавление изображения"""
        background = self.background.copy()
        background = self.drawing_gradient(background=background, weather_data=weather_data)
        save_date = None
        for coordinates, text in zip(self.coordinate_list, self.text_list):
            self.weather_postcard = self.text_on_postcard(text=weather_data[text], coordinates=coordinates,
                                                          background=background)
            save_date = weather_data[text]
        self.weather_postcard[:image.shape[0], :image.shape[1]] = image
        self.save_drawing(save_name=save_date, save_file=self.weather_postcard)
        self.view_image(image=self.weather_postcard, name_of_window='Test')

    def drawing_gradient(self, background, weather_data):
        """Отрисовка градиента"""
        yellow = (0, 255, 255)
        dark_blue = (255, 0, 0)
        blue = (255, 144, 30)
        gray = (38, 38, 38)
        color_dict = {
            'Snow': blue,
            'Rain': dark_blue,
            'Sun': yellow,
            'Cloud': gray
        }
        weather_color = color_dict[weather_data['Погода']]
        count = 0
        colour = 0
        for i in range(255):
            cv2.line(background, (0 + count, 0), (0 + count, 400),
                     (weather_color[0] + i, weather_color[1] + i, weather_color[2] + i), 2)
            count += 3
            colour += 1
        return background

    def save_drawing(self, save_name, save_file):
        """Сохранение открытки"""
        out_path = f'weather_postcard'
        out_path_normalized = os.path.normpath(out_path)
        os.makedirs(out_path_normalized, exist_ok=True)
        cv2.imwrite(os.path.join(out_path_normalized, f'{save_name}.jpg'), save_file)


if __name__ == '__main__':
    weather = WeatherMaker()

