# Куда пойти в Москве

Сайт содержит информацию о самых интересных местах Москвы.

[Демо-версия сайта](http://earlhikky91.pythonanywhere.com/)

## Запуск сайта

Для запуска сайта Python (версия >= 3.6) должен быть установлен.

1. Скачайте код с GitHub.

2. Установите зависимости:

```console
pip install -r requirements.txt
```

3. Определите [переменные окружения](#переменные-окружения).

4. Создайте базу данных SQLite:

```console
python manage.py migrate
```

5. Создайте суперпользователя для доступа в административный интерфейс:

```console
python manage.py createsuperuser
```  

6. Для загрузки [тестовых данных](https://github.com/devmanorg/where-to-go-places/tree/master/places) можно использовать
   пользовательскую management-команду `load_place`:

```console
python manage.py load_place "{url-адрес JSON-файла}"
```

Формат принимаемых входных данных можно посмотреть
в [примере](https://github.com/devmanorg/where-to-go-places/blob/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json)
.

```console
python manage.py load_place "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json"
```   

7. Запустите сервер:

```console
python manage.py runserver
```  

8. [Переход в админку](https://earlhikky91.pythonanywhere.com/admin/):

- login: admin

- password: adminadmin

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и
запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

- `DEBUG=`... - дебаг-режим. По умолчанию `False`.
- `SECRET_KEY=`... - ключ проекта.
- `ALLOWED_HOSTS=`... - см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts), (по
  умолчанию: '127.0.0.1', 'localhost', '.pythonanywhere.com').

## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).  
Тестовые данные взяты с сайта [KudaGo](https://kudago.com/).
