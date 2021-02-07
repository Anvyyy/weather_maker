# WEATHER MAKER

Консольная утилита с помощью которой можно
парсить погодные данные и работать с ними.

Данные парсит с сайта [darksky](https://darksky.net/forecast/40.7127,-74.0059/ca12/en)

![logo](https://www.openhab.org/logos/darksky.png)

### Запустить программу:
Запустить программу можно 
командой из консоли`path/python console.py -command`


### Функционал:

- При включении парсит данные за последние 7 дней с сайта
- Командой `-card` рисует изображения-открытки
  с данными о погоде с помощью библиотеки **opencv**
   
   - Создается градиент под погоду
    - Пишутся данные о погоде
    - Добавляется картинка с погодой
    
- Команда `-db` сохраняет полученные данные в базу данных

   - Если данные уже есть, то они не сохраняются
    
- Команда `-pars` выводит на консоль данные за неделю
- Команда `-get` выводит данные из базы данных
   
   - Напишите команду`-low` и укажите от какой
     даты выводить данные
   - Напишите команду`-hi` и укажите до какой даты
     выводить данные
   -  **!!Дату указывать в формате: день,месяц,год!!**
