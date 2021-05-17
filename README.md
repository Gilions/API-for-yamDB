<p align="center">
  <img width="700" height="323" src="https://user-images.githubusercontent.com/68146917/118408929-8eaa3f80-b690-11eb-8bd9-07e98fcf5913.jpg">
</p>

# API для YAMDB


![yamdb_final](https://github.com/Gilions/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)


**Проект YaMDb** - собирает отзывы (**Review**) пользователей на произведения (**Title**). Произведения делятся на категории:
- «Книги»
- «Фильмы»
- «Музыка»

Список категорий (**Category**) может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (**Review**) и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.

## Техническое описание проекта YaMDb
___

**Пользовательские роли:**
- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь (user)**— может читать всё, как и Аноним, дополнительно может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.
- **Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя плюс право удалять и редактировать любые отзывы и комментарии.
- **Администратор (admin)** — полные права на управление проектом и всем его содержимым. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- **Администратор Django** — те же права, что и у роли Администратор.


## Алгоритм регистрации пользователей
___

1. Пользователь отправляет POST-запрос с параметром email на /api/v1/auth/email/.
2. **YaMDB** отправляет письмо с кодом подтверждения (confirmation_code) на адрес email .
3. Пользователь отправляет POST-запрос с параметрами email и confirmation_code на /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).

Эти операции выполняются один раз, при регистрации пользователя. В результате пользователь получает токен и может работать с API, отправляя этот токен с каждым запросом.
После регистрации и получения токена пользователь может отправить PATCH-запрос на /api/v1/users/me/ и заполнить поля в своём профайле.


## Ресурсы API YaMDb
___
- Ресурс **AUTH**: аутентификация.
- Ресурс **USERS**: пользователи.
- Ресурс **TITLES**: произведения, к которым пишут отзывы (определённый фильм, книга или песенка)
- Ресурс **CATEGORIES**: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс **GENRES**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс **REVIEWS**: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс **COMMENTS**: комментарии к отзывам. Комментарий привязан к определённому отзыву.

## Доступные методы
___
`/api/v1/titles/ (GET, POST)`

`/api/v1/titles/<id>/ (GET, POST, PUT, PATCH, DELETE)`

`/api/v1/titles/<id>/reviews/ (GET, POST)`

`/api/v1/titles/<id>/reviews/<id>/ (GET, POST, PUT, PATCH, DELETE)`

`/api/v1/categories/ (GET, POST)`

`/api/v1/genres/ (GET, POST)`


[Полная версия документация API](https://github.com/yandex-praktikum/api_yamdb/blob/master/static/redoc.yaml)
## Системные требования
____

- [Python 3](https://www.python.org/)
- [Django 3.0.5](https://www.djangoproject.com/)
- [REST API Framework](https://www.django-rest-framework.org/)
- [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [NGINX](https://www.nginx.com/)
- [Gunicorn](https://gunicorn.org/)
- [Docker](https://www.docker.com/)
- [PostgrSQL](https://www.postgresql.org/)

##  Установка
______


Потребуется Pytho3, проверьте версию Вашего Python командой:

`python3 --version`

Для установки Python на операционные системы Linux/Mac используйте команду:

`sudo apt update`

[Установка Python для Windows](https://www.microsoft.com/ru-ru/p/python-37/9nj46sx7x90p?rtc=1&activetab=pivot:overviewtab)



`sudo apt install python3-pip python3-venv git -y`

**Будет установлен:**
- Python3
- venv(виртуальное окружение)
- GitHub


**Клонируйте репозитарий командой:**

`git clone https://github.com/Gilions/yamdb_final.git`

В репозитарии проекта создайте вертуальное окружение:

`python3 -m venv venv & source venv/bin/activate`

Потребуется установка нужных пакетов, используйте:

`python -m pip install -r requirements.txt`

В репозитации необходимо создать файл .env

Внесите следующие данные
```
SECRET_KEY = 'Yours secret key'

DB_NAME = postgres
POSTGRES_USER = postgres
POSTGRES_PASSWORD = Yours password
DB_HOST = localhost
DB_PORT = 5432
```

Запустите проект используя команду:

`python3 manage.py runserver`

## Запуск проекта используя Docker compose:
____
MamOS/windows/Linux:

Потребуется Docker, Docker Compose, v 1.29 +

[Для установки Docker используйте официальную документацию для своей OS](https://docs.docker.com/compose/install/)

Измените сожержимое файл .env на:

```
SECRET_KEY = 'Yours Key

DB_NAME = postgres
POSTGRES_USER = postgres
POSTGRES_PASSWORD = Yours password
DB_HOST = db
DB_PORT = 5432
```
Для запуска проекта необходимо использовать файл docker-compose.yaml из
репозитария.

Используйте команду находясь в одной директории с файлом docker-compose.yaml:

`docker-compose up`

## Участники
___

- [Vitaly Sofronyuk](https://github.com/Gilions) - категории (Categories), жанры (Genres) и произведения (Titles):
    + модели и view;
    + эндпойнты;
    + рейтинги произведений;
    + права доступа для запросов.
- [Pavel Yasukevich](https://github.com/PavelYasukevich) - управление пользователями (Auth и Users):
    + система регистрации и аутентификации;
    + права доступа, работа с токеном;
    + система подтверждения e-mail, поля.
- [blanksearch](https://github.com/blanksearch) - отзывы (Review) и комментарии (Comments):
    + модели и view;
    + эндпойнты;
    + права доступа для запросов.
