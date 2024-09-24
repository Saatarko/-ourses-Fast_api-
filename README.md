# Этот проект - дипломная работа студента группы Py53-onl Хвороща Александр Владимировича.

# Ссылка на сайт:
-

# Описание:
REST Backend  IT школы с курсами, записями на курсы,зачислением в группы и групповым чатом на websocket.Реализована отправка почты после создания записи в таблице (как просто отпаавкой так и через Celery). Сделано кеширование. Как и Celery настроено для работы с Redis.

# Frontend:

Вместо Frontend - внешнее приложение на Kivi
https://github.com/Saatarko/kivy_app.git

# Технологии:

Языки программирования: Python v3.10
Дополнительно: Celery, Redis
Framework: Fastapi
Database: SQLLite

# Размещение:
-

# Для локальной загрузки требуется:
1. Загрузить сайт на ПК.
2. Установить виртуальное окружение с Python v3.10
3. Установить библиотеки. (в проекте использовался poetry)
   Для этого Вам нужно установить poetry - pip install poetry
   Затем для устновки всех библиотек  -   poetry install
4. Для запуска локально нужно раскоментировать в main.py
    if __name__ == "__main__":
    uvicorn.run("main:main_app", host="127.0.0.1", port=8000, reload=True)
    
   Дополнительно. Команда длля запуска сайта на сервере или через Docker (нужно убедиться что строки 
   if __name__ == "__main__":
    uvicorn.run("main:main_app", host="127.0.0.1", port=8000, reload=True)
   закоментированы или удалены) а затем
   
# Команда для запуска приложения
CMD ["poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main.app", "--bind", "0.0.0.0:8000"]




# This project is a diploma of the student of the Py53-onl group Khvorosh Alexander Vladimirovich.

# Link to the site:
-

# Description:
REST Backend of an IT school with courses, course registration, group enrollment and group chat on websocket. Implemented sending mail after creating a record in the table (both by simply sending and via Celery). Caching is done. Like Celery, it is configured to work with Redis.

# Frontend:

Instead of Frontend - an external application on Kivi
https://github.com/Saatarko/kivy_app.git

# Technologies:

Programming languages: Python v3.10
Additional: Celery, Redis
Framework: Fastapi
Database: SQLLite

# Placement:
-

# For local download you need:
1. Download the site to your PC.
2. Install a virtual environment with Python v3.10
3. Install libraries. (poetry was used in the project)
To do this, you need to install poetry - pip install poetry
Then to install all the libraries - poetry install
4. To run locally, you need to uncomment in main.py
if __name__ == "__main__":
uvicorn.run("main:main_app", host="127.0.0.1", port=8000, reload=True)

Additionally. Command to run the site on the server or via Docker (you need to make sure that the lines
if __name__ == "__main__":
uvicorn.run("main:main_app", host="127.0.0.1", port=8000, reload=True)
are commented out or removed) and then

# Command to run the application
CMD ["poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main.app", "--bind", "0.0.0.0:8000"]

