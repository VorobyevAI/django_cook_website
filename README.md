<h2 align="center">Cook website</h2>

### Описание проекта:
Блог шеф-повара с рецептами


### Инструменты разработки

**Стек:**
- Python >= 3.10.4
- Django == 4.1.6
- sqlite3

## Разработка

##### 1) Поставить звездочку)

##### 2) Клонировать репозиторий

    git clone https://github.com/DJWOMS/cook_blog.git

##### 3) Создать виртуальное окружение

    cd cook_blog
    
    python -m venv venv
    
##### 4) Активировать виртуальное окружение
    
Linux

    source venv/bin/activate
    
Windows

    ./venv/Scripts/activate

##### 5) Устанавливить зависимости:

    pip install -r req.txt

##### 6) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 8) Создать суперпользователя

    python manage.py createsuperuser
    
##### 9) Запустить сервер

    python manage.py runserver

##### 10) Ссылки

- Сайт http://127.0.0.1:8000/

- Админ панель http://127.0.0.1:8000/admin

## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2021-present, Smad - Andrey Vorobyev



