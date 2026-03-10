# Friends Album Django Project

This is simple Django project using PostgreSQL.

## Setup
В проекта използвам .env за SECRET_KEY и DB_PASSWORD.
В GitHub е качен само примерният файл .env.example.
Копирайте .env.example в .env: copy .env.example .env
и попълнете свои тестови стойности в .env
Останалите настройки на базата (DB_NAME, DB_USER, DB_HOST, DB_PORT) са вече в settings.py.

#```bash
#pip install -r requirements.txt
#python manage.py migrate
#python manage.py runserver