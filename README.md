<h1 align="center">Сайт постов</h1>
<p>

Это простой сайт постов.
С возможностями добавления, удаления и обновления постов. 
</p>

**Стек:**
- Python >= 3.11
- Django==4.1.6
- sqlite3
---
<h3>Руководство по устоновке:</h3>

#### 1) Скалинируте репозиторий
    git clone https://github.com/Raasaal511/post_save/

#### 2) Создать виртульное окружение
     pip -m venv venv

#### 3) Актвировать веруальное окружение (если оно не активировалось)
###### (windows)
    cd venv/scripts
    activate

#### 4) Устанавливить зависимости:
    pip install -r requirements.txt

#### 4) Сделайте миграцию:
    python manage.py makemigrations
    python manage.py migrate

#### 4) Создайте супер пользвателя:
    python manage.py createsuperuser
