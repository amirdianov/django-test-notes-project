# django 2k 11-100

Для работы с проектом нужно установить [python](http://python.org) и
[poetry](https://python-poetry.org/).

- `docker-compose up -d` - поднять PostgreSQL с помощью Docker
- `poetry shell` - вход в виртуальное окружение
- `poetry install` - установка зависимостей
- `python src/manage.py migrate` - выполнить миграции
- `python src/manage.py runserver` - запуск сервера для разработки на http://localhost:8000
- `pytest` - запустить автоматические тесты