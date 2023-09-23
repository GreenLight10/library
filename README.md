# <p align="center"> Цифрвовой прорыв: сезон ИИ </p>
## <p align="center"> Кейс: Распознавание деталей/узлов на участке </p>


*Состав команды "гИИрлянда"*   
*Михайлов Сергей*    
*Громогласов Валерий*  
*Габов Владимир*  

## <a name="1"> Задание </a>

На производстве присутствует так называемый участок окраски. На этот участок следуют идентифицируемые детали и узлы (путем нанесенной на них гравировки или имеющейся бирки). Проблема идентификации будет заключаться в том, что перед покраской бирки снимаются, а гравюры закрашиваются в процессе покраски. В результате чего имеется множество неидентифицированных деталей, а на их идентификацию, при высокой загрузке, тратится большое количество времени и ресурсов. Сегодня же можно распознавать покрашенные детали при помощи технологий компьютерного зрения, опираясь на характеристики детали и ее 3Д-модель. В следствие чего участникам хакатона предлагается разработать прототип системы распознавания окрашенных деталей и узлов (например при наведении камеры телефона), а также развить решение задачи в сторону отображения дополнительной информации о детали при таком распознавании (например характеристики и тд).


## <a name="2">Запуск </a>

Модель нейросети в проекте уже обучена, поэтому для использования необходимо установить необходимые библиотеки для локального запуска без обучения сети

Для запуска нейросети на локальном сайте необходимо:
Открыть терминал и вписать следуюшие строки:
1. Склонировать репозиторий `git clone`
2. Войти в папку с проектом `cd project`
3. В папке проекта выполнить команду `python -m venv env`
4. Активировать виртуальную среду `env\Scripts\activate.bat`

Скачать необходимые библиотеки и фреймворки вписав в терминал:

1. `pip install django`
2. `pip install h5py`
3. `pip install opencv-python`
4. `pip install Pillow`
5. `pip install tensorflow`
6. `pip install keras`
7. `pip install matplotlib`

Запустим локальный сервер:

1. Пишем в терминал `python manage.py runserver`
2. Зайти на `http://127.0.0.1:8000/` в браузере.

На сайте загружаем файл для идентификации детали и нажимаем ...
