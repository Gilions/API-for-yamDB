# API для YAMDB

CI/CD API for Yatube
![yamdb_final](https://github.com/Gilions/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)


API для базы данных YAMDB, база данных содержит оставленные комментарии о фильмах, книгах и музыке. 

Формирует средний рейтинг произведений.

Данный проект разрабатывался в рамках обучающей программы курсов Yandex Практикум.
Цель данного проекта, изучить возможность REST API

##  Установка
______


Потребуется Pytho3, проверьте версию Вашего Python командой:

`python3 --version`

Для установки Python на операционные системы Linux/Mac используйте команду:

`sudo apt update`

Для установки Python на Windows пройдите по ссылке

https://www.microsoft.com/ru-ru/p/python-37/9nj46sx7x90p?rtc=1&activetab=pivot:overviewtab

`sudo apt install python3-pip python3-venv git -y`

Будет установлен: Python3, venv(виртуальное окружение), GitHub


Клонируйте репозитарий командой:

`git clone https://github.com/Gilions/yamdb_final.git`

В репозитарии проекта создайте вертуальное окружение:

`python3 -m venv venv & source venv/bin/activate`

Потребуется установка нужных пакетов, используйте:

`python -m pip install -r requirements.txt` 

Запустите проект используя команду:

`python3 manage.py runserver`

## Запуск проекта используя Docker compose:
____
MamOS/windows/Linux:

Потребуется Docker, Docker Compose, v 1.29 +

Для установки Docker используйте официальную документацию для своей OS
https://docs.docker.com/compose/install/

Для запуска проекта необходимо использовать файл docker-compose.yaml из
репозитария.

Используйте команду находясь в одной директории с файлом docker-compose.yaml:

`docker-compose up`

## Важно

Для успешного запуска, Вам нужно создать файл .env, в котором указать параметры подключаемой БД, в проекте по умолчанию используется PostgreSQL.
